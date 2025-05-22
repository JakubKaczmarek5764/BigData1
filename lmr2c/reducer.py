#!/usr/bin/python3.12
"""reducer.py"""

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
        if data_type == "SZCZEPIENI":
            vaccinated_data[country].extend(map(int, value.split(',')))
        elif data_type == "POPULACJA":
            population_data[country] = int(value)
    except ValueError:
        continue

# Obliczanie procentu zaszczepionych
for country, vaccinated_list in vaccinated_data.items():
    max_vaccinated = max(vaccinated_list, default=0)
    population = population_data.get(country, 0)
    if population > 0 and max_vaccinated < population and max_vaccinated > 0:
        vaccinated_percentage = (max_vaccinated / population) * 100
        print(f"{country}\t{vaccinated_percentage:.2f}%")
