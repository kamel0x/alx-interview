#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics
"""

import re
from sys import stdin, stdout


def extract_input(input_line):
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    resp_match = re.fullmatch(log_fmt, input_line)
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


try:
    num = 0
    status_dict = {}
    total_size = 0
    while True:
        line = input()

        info = extract_input(line)
        num += 1
        total_size += int(info['file_size'])
        status = info['status_code']
        if status in status_dict:
            status_dict[status] += 1
        else:
            status_dict[status] = 1
        if num % 10 == 0:
            print("File size: {}".format(total_size), flush=True)
            for key, value in sorted(status_dict.items()):
                print(f"{key}: {value}", flush=True)
except (KeyboardInterrupt, EOFError):
    print(f"File size: {total_size}", flush=True)
    for key, value in sorted(status_dict.items()):
        print(f"{key}: {value}", flush=True)
