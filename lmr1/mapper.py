#!/usr/bin/python3.12
"""mapper.py"""

import sys

for line in sys.stdin:
    line = line.strip()
    id, country, cases = line.split(',')
    if id:
        print('%s\t%s' % (country, cases))
