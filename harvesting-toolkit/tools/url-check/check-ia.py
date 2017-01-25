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

__version__ = '0.11'
__author__  = 'Michael Hucka <mhucka@caltech.edu>'
__email__   = 'mhucka@caltech.edu'
__license__ = 'Public domain'

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

def run(input_file, urls, found_file, notfound_file, quiet=False):
    successes = []
    failures  = []

    if input_file:
        with open(input_file, encoding="utf-8") as f:
            for line in f:
                url = line.strip()
                if '/' not in url:             # Skip non-URLs
                    continue
                (found, result) = check(url, quiet)
                if found:
                    successes.append(result)
                else:
                    failures.append(url)
    else:
        for url in urls:
            (found, result) = check(url, quiet)
            if found:
                successes.append(result)
            else:
                failures.append(url)

    if not quiet and (successes or failures):
        msg('-'*70)
    if successes:
        if found_file:
            with open(found_file, 'w') as out:
                count = 0
                for entry in successes:
                    out.write(entry[0])
                    out.write(',')
                    out.write(entry[1])
                    out.write(',')
                    out.write(entry[2])
                    out.write('\n')
                    count += 1
            if not quiet:
                msg('{} successes written to file "{}"'.format(count, found_file))
        else:
            msg('{} URLs found in IA'.format(len(successes)))
    elif not quiet:
        if found_file:
            msg('No successes -- {} not written'.format(found_file))
        else:
            msg('No successes')
    if failures:
        if notfound_file:
            with open(notfound_file, 'w') as out:
                count = 0
                for url in failures:
                    out.write(url)
                    out.write('\n')
                    count += 1
            if not quiet:
                msg('{} failures written to file "{}"'.format(count, notfound_file))
        else:
            msg('{} URLs not found in IA'.format(len(failures)))
    elif not quiet:
        if notfound_file:
            msg('No failures -- {} not written'.format(notfound_file))
        else:
            msg('No failures')


# Utilities
# ......................................................................

def check(given_url, quiet=False):
    final_url = get_final_url(given_url)
    if not final_url:
        if not quiet:
            msg('Could not access {} -- skipping'.format(given_url))
        return (False, given_url)
    url = 'http://archive.org/wayback/available?url=' + final_url
    try:
        response = urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        if data['archived_snapshots']:
            archive_info = data['archived_snapshots']
            if 'closest' not in archive_info:
                if not quiet:
                    msg('Got unexpected result for {}'.format(given_url))
                return (False, given_url)
            ts = archive_info['closest']['timestamp']
            status = archive_info['closest']['status']
            ia_url = archive_info['closest']['url']
            if not quiet:
                if int(status) > 300:
                    msg('*** abnormal status {} for {}'.format(status, given_url))
                else:
                    msg('Found: {}'.format(ts, given_url))
            return (True, (ts, given_url, ia_url))
        else:
            if not quiet:
                msg('Not found: {}'.format(given_url))
            return (False, given_url)
    except Exception as e:
        msg('Unable to check {}'.format(given_url))
        msg(e)
        return (False, given_url)


def get_final_url(url):
    try:
        requests.packages.urllib3.disable_warnings()
        resp = requests.get(url, verify=False, timeout=10)
        if resp.history:
            return resp.history[-1].url
        elif url[-1] != '/':
            url = url + '/'
            return get_final_url(url)
        else:
            # See if the host has a number in the name, like "www3.epa.gov".
            # Remove the number and try again.
            u = urlparse(url)
            if re.search('\d', u.netloc):
                loc = re.sub('[0-9]', '', u.netloc)
                url = u.scheme + '://' + loc + u.path
                return get_final_url(url)
        # If we get here, all our attempts failed.  Leave the URL as it was
        # and hope for the best.
        return url
    except Exception as e:
        msg('Encountered problem dereferencing {}'.format(url))
        msg(e)


def msg(text):
    print(text, flush=True)


# Entry point
# ......................................................................

def cli_interface():
    plac.call(main)

cli_interface()
