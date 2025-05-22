#!/usr/bin/python3.12
"""combiner.py"""

import sys
from collections import defaultdict

# Pamiętaj dane jako wartości lokalne
combined_data = defaultdict(list)

# Proces lokalny dla surowych wejściowych par (kraj, squashed_lists)
for line in sys.stdin:
    line = line.strip()
    try:
        country, value = line.split('\t')
        cases, timestamp = map(int, value.split(','))
        combined_data[country].append((cases, timestamp))
    except ValueError:
        continue

# Emitowanie kombinowanych lokalnych list jako wartości dla reduktora
for country, values in combined_data.items():
    print(f"{country}\t{values}")