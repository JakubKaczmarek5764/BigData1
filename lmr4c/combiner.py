#!/usr/bin/python3.12
"""combiner.py"""

import sys
from collections import defaultdict

combined_data = defaultdict(list)

for line in sys.stdin:
    line = line.strip()
    try:
        country, value = line.split('\t')
        cases, timestamp = map(int, value.split(','))
        combined_data[country].append((cases, timestamp))
    except ValueError:
        continue

for country, values in combined_data.items():
    print(f"{country}\t{values}")