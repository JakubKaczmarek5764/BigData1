#!/usr/bin/python3.12
"""mapper.py"""

import sys

for line in sys.stdin:
    line = line.strip()
    parts = line.split(',')

    if len(parts) == 4:
        country = parts[1].strip()
        try:
            cumulative_vaccinated = int(parts[3].strip())
            print(f"{country}\tSZCZEPIENI\t{cumulative_vaccinated}")
        except ValueError:
            continue

    elif len(parts) == 2:
        country = parts[0].strip()
        try:
            population = int(parts[1].strip())
            print(f"{country}\tPOPULACJA\t{population}")
        except ValueError:
            continue