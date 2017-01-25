#!/usr/bin/env python3
'''
check-ia.py: check if a given URL is in the Internet Archive.

Usage:
   check-ia.py urlfile [failuresfile] [successesfile]

This uses the Wayback Machine API to test if a given URL is in IA.  It will
iterate over the URLs in a given file and check each one individually, then
print success or failure.  If given an optional 2nd command line argument,
a file name, it will write the failures to that file at the end.  If an
optional 3rd argument is given, it should be the name of another file to
which the successes are written.

In order to account for possible redirections, it first queries the original
URL.  This means every URL will cause a hit to the original source location
as well as the Wayback Machine's API server.

Further reading:
Wayback Machine API description: https://archive.org/help/wayback_api.php

'''

__version__ = '1.0'
__author__  = 'Michael Hucka <mhucka@caltech.edu>'
__email__   = 'mhucka@caltech.edu'
__license__ = 'Public domain'

import colorama
import http
import json
import os
import plac
import re
import requests
import sys
from time import sleep
from urllib.request import urlopen
from urllib.parse import urlparse


# Command line interface
# ......................................................................

def main(file=None, okay=None, miss=None, quiet=False, *args):
    # Check for valid arguments.
    if file and args:
        raise ValueError("Can't supply both input file and URLs on command line")
    elif not file and not args:
        raise ValueError('No input file and no URLs given -- nothing to do')
    elif file and not os.path.exists(file):
        raise ValueError('File "{}" not found'.format(file))
    if not quiet:
        colorama.init(autoreset=True)
    # Let's do this thing.
    run(file, args, okay, miss, quiet)

# Plac annotations for main function arguments.
# Argument annotations are: (help, kind, abbrev, type, choices, metavar).
# Plac automatically adds a -h argument for help, so no need to do it here.
#
main.__annotations__ = dict(
    file  = ('input file to read for URLs to check',      'option', 'f'),
    okay  = ('output file to write URLs found in IA',     'option', 'o'),
    miss  = ('output file to write URLs missing from IA', 'option', 'm'),
    quiet = ('quiet -- do not echo every check',          'flag',   'q'),
    args  = '(optional) URLs on the command line',
)


# Main functions
# ......................................................................

def run(input_filename, urls, found_filename, notfound_filename, quiet=False):
    found_file     = None
    found_count    = 0
    notfound_file  = None
    notfound_count = 0

    if found_filename:
        found_file = open(found_filename, 'w')
    if notfound_filename:
        notfound_file = open(notfound_filename, 'w')

    if input_filename:
        with open(input_filename, encoding="utf-8") as f:
            for idx, line in enumerate(f):
                url = line.strip()
                if '/' not in url:             # Skip non-URLs
                    continue
                if check(url, idx, found_file, notfound_file, quiet):
                    found_count += 1
                else:
                    notfound_count += 1
    else:
        for idx, url in enumerate(urls):
            if check(url, idx, found_file, notfound_file, quiet):
                found_count += 1
            else:
                notfound_count += 1

    if not quiet and (found_count > 0 or notfound_count > 0):
        print('')
    if found_filename:
        found_file.close()
        if not quiet:
            if found_count:
                info('{} URLs found, written to file "{}"'.format(found_count, found_filename))
            else:
                info('No URLs found.')
    elif found_count > 0 and not quiet:
        info('{} URLs found'.format(found_count))
    if notfound_filename:
        notfound_file.close()
        if not quiet:
            if notfound_count:
                info('{} URLS not found, written to file "{}"'.format(notfound_count, notfound_filename))
            else:
                info('All URLs found')
    elif notfound_count > 0 and not quiet:
        info('{} URLs not found'.format(notfound_count))
    if not quiet:
        info('Done.')
        print(colorama.Style.RESET_ALL)


# Utilities
# ......................................................................

def check(given_url, idx, found_file, notfound_file, quiet=False):
    try:
        (found, ts, ia_url, status) = url_in_ia(given_url)
        if not found:
            # Try to dereference the original URL, in case the origin
            # server redirects to another URL and that's what IA has.
            final_url = get_final_url(given_url)
            (found, ts, ia_url, status) = url_in_ia(final_url)
        if not found:
            warning('[{}] {} -- not found in IA'.format(idx, given_url))
            log(notfound_file, given_url)
            return False
        elif not ts:
            warning('[{}] {} -- found, but no data available'.format(idx, given_url))
            log(found_file, given_url, '00000000000000')
            return True
        elif int(status) > 300:
            warning('[{}] {} -- found, but IA record has status {}'.format(idx, given_url, status))
            log(notfound_file, given_url)
            return False
        else:
            good('[{}] {} -- archived {}'.format(idx, given_url, ts))
            log(found_file, given_url, ts)
            return True
    except Exception as e:
        bad('Unable to check {}'.format(given_url))
        bad(str(e))
        return False


def url_in_ia(url):
    '''Returns a tuple: (found, timestamp, archived_url, status_code)
    where "found" is a Boolean indicating whether the URL was found in IA,
    and the remaining tuple values are the data found in IA if the URL was
    indeed found.'''

    test_url = 'http://archive.org/wayback/available?url=' + url
    response = urlopen(test_url)
    data = json.loads(response.read().decode('utf-8'))
    if 'archived_snapshots' in data:
        archive_info = data['archived_snapshots']
        if 'closest' not in archive_info:
            # This can happen when IA reports positively for the URL but
            # provides no additional data.  According to the API docs, this
            # happens "If the url is not available (not archived or currently
            # not accessible)"; however, I have seen it happen when an
            # archived URL is a redirection to another page within IA itself.
            # Example case: https://www3.epa.gov/node/156853
            # To avoid false positives, we treat this as a failure, but we
            # need to tell IA about this ambiguity.
            return (False, None, None, None)
        ts = archive_info['closest']['timestamp']
        ia_url = archive_info['closest']['url']
        status = archive_info['closest']['status']
        return (True, ts, ia_url, status)
    else:
        return (False, None, None, None)


def get_final_url(url):
    '''Attempt to read the given "url" using HTTP HEAD and return the
    final URL after any redirections.'''

    def get_head(url):
        return requests.head(url, allow_redirects=True, verify=False, timeout=10)

    try:
        requests.packages.urllib3.disable_warnings()
        resp = get_head(url)
        if resp.history:
            return resp.history[-1].url
        elif url[-1] != '/':
            url = url + '/'
            return get_final_url(url)
        else:
            # See if the host has a number in the name, like "www3.epa.gov".
            u = urlparse(url)
            if re.search('\d', u.netloc):
                # Remove the number and try again.
                loc = re.sub('[0-9]', '', u.netloc)
                url = u.scheme + '://' + loc + u.path
                # This time, we don't want to go through the rediretion step
                # because it'll probably send us back to the original.
                resp = get_head(url)
                if resp.history:
                    return url
        # If we get here, all our attempts failed.  Leave the URL as it was
        # and hope for the best.
        return url
    except Exception as e:
        bad('Encountered problem dereferencing {}'.format(url))
        bad(str(e))


def log(dest_file, *args):
    if dest_file:
        dest_file.write(','.join(args) + '\n')


def bad(text):
    print(colorama.Fore.RED + text, flush=True)


def good(text):
    print(colorama.Fore.GREEN + text, flush=True)


def warning(text):
    print(colorama.Fore.YELLOW + text, flush=True)


def info(text):
    print(text, flush=True)


# Entry point
# ......................................................................

def cli_interface():
    plac.call(main)

cli_interface()
