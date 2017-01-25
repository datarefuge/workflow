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
import re
import requests
import sys
from time import sleep
from urllib.request import urlopen
from urllib.parse import urlparse

if len(sys.argv) < 2:
    print('Missing argument: file containing list of URLs to check')
    sys.exit(1)

failures_file  = sys.argv[2] if len(sys.argv) > 2 else None
successes_file = sys.argv[3] if len(sys.argv) > 3 else None


# Utility functions
# ......................................................................

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


# Main loop
# ......................................................................

successes = []
failures  = []
delay     = 0

msg('Starting.')
msg('Reading URLs from file "{}"'.format(sys.argv[1]))
if failures_file:
    msg('Writing failures to file "{}"'.format(failures_file))
else:
    msg('Not writing failures to a file')
if successes_file:
    msg('Writing successes to file "{}"'.format(successes_file))
else:
    msg('Not writing successes to a file')
msg('Using a delay of {}'.format(delay))
msg('')

with open(sys.argv[1], encoding="utf-8") as f:
    for i, line in enumerate(f):
        line = line.strip()
        if '/' not in line:             # Check blank lines.
            continue
        final_url = get_final_url(line)
        if not final_url:
            msg('Could not access {} -- skipping'.format(line))
            continue
        url = 'http://archive.org/wayback/available?url=' + final_url
        try:
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))
            i = i + 1                   # Start line numbering at 1.
            if data['archived_snapshots']:
                archive_info = data['archived_snapshots']
                if 'closest' not in archive_info:
                    msg('Got unexpected result for {}'.format(line))
                    failures.append(line)
                    continue
                ts = archive_info['closest']['timestamp']
                status = archive_info['closest']['status']
                ia_url = archive_info['closest']['url']
                successes.append((ts, line, ia_url))
                if int(status) > 300:
                    msg('[{}] {} -- abnormal status {}'.format(i, line, status))
                else:
                    msg('[{}] {} -- archived {}'.format(i, line, ts))
            else:
                msg('[{}] {} -- not archived'.format(i, line))
                failures.append(line)
        except Exception as e:
            msg('Unable to check {}'.format(line))
            msg(e)
    if type(delay) == int and delay > 0:
        sleep(delay)


msg('Done.')

if successes_file:
    if successes:
        msg('-'*70)
        with open(successes_file, 'w') as out:
            for entry in successes:
                out.write(entry[0])
                out.write(',')
                out.write(entry[1])
                out.write(',')
                out.write(entry[2])
                out.write('\n')
        msg('Successes written to file "{}"'.format(successes_file))
else:
    msg('No successes -- {} not written'.format(successes_file))

if failures:
    msg('-'*70)
    if failures_file:
        with open(failures_file, 'w') as out:
            for url in failures:
                out.write(url)
                out.write('\n')
        msg('Failures written to file "{}"'.format(failures_file))
    else:
        msg('The following URLs were not found or produced unexpected results:')
        for url in failures:
            msg(url)
