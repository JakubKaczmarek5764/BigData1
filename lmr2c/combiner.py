#!/usr/bin/python3.12
"""combiner.py"""

import sys
from collections import defaultdict

vaccinated_data = defaultdict(list)
population_data = {}

for line in sys.stdin:
    line = line.strip()
    parts = line.split('\t')

    if len(parts) != 3:
        continue

    country, data_type, value = parts[0], parts[1], parts[2]

    try:
        value = int(value)
    except ValueError:
        continue

    if data_type == "SZCZEPIENI":
        vaccinated_data[country].append(value)
    elif data_type == "POPULACJA":
        population_data[country] = value

for country, vaccinated_list in vaccinated_data.items():
    print(f"{country}\tSZCZEPIENI\t{','.join(map(str, vaccinated_list))}")
for country, population in population_data.items():
    print(f"{country}\tPOPULACJA\t{population}")