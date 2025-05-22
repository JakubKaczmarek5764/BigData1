#!/usr/bin/python3.12
"""reducer.py"""

import sys

current_country = None
max_vaccinated = 0
population = 0

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


    if current_country and country != current_country:
        if population > 0 and max_vaccinated > 0 and max_vaccinated <= population:
            vaccinated_percentage = (max_vaccinated / population) * 100
            print(f"{current_country}\t{vaccinated_percentage:.2f}%")

        max_vaccinated = 0
        population = 0

    current_country = country

    if data_type == "SZCZEPIENI":
        max_vaccinated = max(max_vaccinated, value)
    elif data_type == "POPULACJA":
        population = value

if current_country:
    if population > 0 and max_vaccinated > 0 and max_vaccinated <= population:
        vaccinated_percentage = (max_vaccinated / population) * 100
        print(f"{current_country}\t{vaccinated_percentage:.2f}%")
    
