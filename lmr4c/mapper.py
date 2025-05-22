#!/usr/bin/python3.12
"""mapper.py"""

import sys

# Przetwarzanie danych wejściowych w Mapperze
for line in sys.stdin:
    try:
        line = line.strip()
        parts = line.split(',')

        if len(parts) < 3 or not parts[2].isdigit():  # Pomijamy niepoprawne wiersze
            continue

        country = parts[1]  # Nazwa kraju
        cases = int(parts[2])  # Liczba nowych przypadków
        print(f"{country}\t{cases}")  # Format wyjścia klucz\twartość
    except Exception:
        continue