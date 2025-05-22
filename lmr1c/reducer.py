#!/usr/bin/python3.12
"""reducer.py"""

import sys

current_country = None
current_cases = 0

for line in sys.stdin:
    line = line.strip()
    country, cases = line.split('\t')
    try:
        cases = int(cases)
    except ValueError:
        continue
    
    if current_country == country:
        current_cases += cases
    else:
        if current_country:
            print(f"{current_country}\t{current_cases}")
        current_cases = cases
        current_country = country

if current_country:
    print(f"{current_country}\t{current_cases}")
