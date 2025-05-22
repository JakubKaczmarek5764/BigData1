#!/usr/bin/python3.12
"""mapper.py"""

import sys

for line in sys.stdin:
    line = line.strip()
    parts = line.split(',')

    # Emitowanie wartości dotyczących szczepień
    if len(parts) == 4:
        country = parts[1].strip()  # country_name_x
        try:
            cumulative_vaccinated = int(parts[3].strip())  # cumulative_persons_vaccinated
            print(f"{country}\tSZCZEPIENI\t{cumulative_vaccinated}")
        except ValueError:
            continue  # Pomijamy błędne dane

    # Emitowanie danych populacyjnych
    elif len(parts) == 2:
        country = parts[0].strip()  # country
        try:
            population = int(parts[1].strip())  # population
            print(f"{country}\tPOPULACJA\t{population}")
        except ValueError:
            continue  # Pomijamy błędne dane