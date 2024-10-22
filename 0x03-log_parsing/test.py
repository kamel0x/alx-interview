#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics
"""
import re
from sys import stdin, stdout

try:
    num = 0
    status_dict = {}
    total_size = 0
    while True:
        line = input()
        pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+) - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] "(GET|POST|PUT|DELETE) (/.+?) HTTP/\d\.\d" (\d+) (\d+)$')
        
        line = pattern.match(line)
        if line:
            num += 1
            ip = line.group(1)
            status = line.group(5)
            file_size = line.group(6)
            total_size += int(file_size)
            if status in status_dict:
                status_dict[status] += 1
            else:
                status_dict[status] = 1
            if num % 10 == 0:
                print("File size: {}".format(total_size), flush=True)
                for key, value in status_dict.items():
                    print(f"{key}: {value}", flush=True)
except (KeyboardInterrupt, EOFError):
    print(f"File size: {total_size}", flush=True)
    for key, value in status_dict.items():
        print(f"{key}: {value}", flush=True)
