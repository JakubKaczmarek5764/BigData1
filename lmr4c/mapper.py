#!/usr/bin/python3.12
"""mapper.py"""

import sys

for line in sys.stdin:
    try:
        line = line.strip()
        parts = line.split(',')
        if len(parts) < 5 or not parts[2].isdigit() or not parts[4].isdigit():
            continue
        country = parts[1]
        cases = int(parts[2])
        timestamp = int(parts[4])
        print(f"{country}\t{cases},{timestamp}")
    except Exception:
        continue