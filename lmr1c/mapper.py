#!/usr/bin/python3.12
"""mapper.py"""

import sys

for line in sys.stdin:
    try:
        line = line.strip()
        parts = line.split(',')
        if len(parts) < 3 or not parts[2].isdigit():
            continue
        country = parts[1]
        cases = int(parts[2])
        print(f"{country}\t{cases}")
    except Exception as e:
        continue
