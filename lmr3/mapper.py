#!/usr/bin/python3.12
"""mapper.py"""

import sys

for line in sys.stdin:
    line = line.strip()
    parts = line.split(',')
    
    # Pomijamy pierwszy wiersz (nagłówki pliku CSV)
    if parts[0] == "":
        continue

    try:
        country = parts[1].strip()
        confirmed = int(parts[2].strip())
        deceased = int(parts[3].strip())
        print(f"{country}\t{confirmed}\t{deceased}")
    except ValueError:
        # Jeśli wystąpi błąd w danych wejściowych, pomiń wiersz
        continue
