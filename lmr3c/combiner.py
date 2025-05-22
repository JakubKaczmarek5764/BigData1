#!/usr/bin/python3.12
"""combiner.py"""

import sys

current_country = None
country_confirmed = 0
country_deceased = 0

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

    # Jeśli zmieniamy kraj, emituj dane częściowo zsumowane
    if current_country and current_country != country:
        print(f"{current_country}\t{country_confirmed}\t{country_deceased}")
        # Resetowanie danych dla nowego kraju
        country_confirmed = 0
        country_deceased = 0

    current_country = country
    country_confirmed += confirmed
    country_deceased += deceased

# Emituj dane dla ostatniego kraju
if current_country:
    print(f"{current_country}\t{country_confirmed}\t{country_deceased}")