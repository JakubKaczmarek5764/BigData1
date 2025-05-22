#!/usr/bin/python3.12
"""mapper.py"""

# mapper.py
import sys
import json

for line in sys.stdin:
    try:
        line = line.strip()
        parts = line.split(',')
        if len(parts) < 3 or not parts[2].isdigit():  # Pomiń niepoprawne wiersze
            continue
        country = parts[1]  # Nazwa kraju
        cases = int(parts[2])  # Liczba nowych przypadków
        print(f"{country}\t{cases}")
    except Exception as e:
        continue
