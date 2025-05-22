#!/usr/bin/python3.12
"""combiner.py"""

import sys
from collections import defaultdict

aggregated_data = defaultdict(list)

for line in sys.stdin:
    line = line.strip()
    country, cases = line.split('\t')
    cases = int(cases)
    aggregated_data[country].append(cases)

for country, cases_list in aggregated_data.items():
    print(f"{country}\t{','.join(map(str, cases_list))}")