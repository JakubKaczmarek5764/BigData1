#!/usr/bin/python3.12
"""reducer.py"""

import sys

current_country = None
total_confirmed = 0
total_deceased = 0

for line in sys.stdin:
    line = line.strip()
    parts = line.split('\t')

    if len(parts) != 3:
        continue

    country, confirmed, deceased = parts[0], parts[1], parts[2]

    try:
        confirmed = int(confirmed)
        deceased = int(deceased)
    except ValueError:
        continue

    if current_country and current_country != country:
        if total_confirmed > 0:
            death_percentage = (total_deceased / total_confirmed) * 100
            print(f"{current_country}\t{death_percentage:.2f}%")
        total_confirmed = 0
        total_deceased = 0

    current_country = country
    total_confirmed += confirmed
    total_deceased += deceased

if current_country:
    if total_confirmed > 0:
        death_percentage = (total_deceased / total_confirmed) * 100
        print(f"{current_country}\t{death_percentage:.2f}%")