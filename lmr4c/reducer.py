#!/usr/bin/python3.12
"""reducer.py"""

import sys
from collections import defaultdict
from math import sqrt
from itertools import combinations


def cosine_similarity(vecA, vecB):
    dot_product = sum(a * b for a, b in zip(vecA, vecB))
    magnitude_a = sqrt(sum(a * a for a in vecA))
    magnitude_b = sqrt(sum(b * b for b in vecB))
    if magnitude_a == 0 or magnitude_b == 0:
        return 0
    return dot_product / (magnitude_a * magnitude_b)


country_vectors = defaultdict(list)

# Przetwarzanie danych wejściowych od combinerów
for line in sys.stdin:
    line = line.strip()
    try:
        country, values = line.split('\t')
        values = eval(values)  # Konwersja stringa na listę tupli
        country_vectors[country].extend(values)
    except ValueError:
        continue

# Sortowanie tupli dla każdego kraju na podstawie znacznika czasu
for country in country_vectors:
    country_vectors[country] = sorted(country_vectors[country], key=lambda x: x[1])

# Przygotowanie wektorów przypadków dla obliczeń
country_case_vectors = {k: [cases for cases, _ in v] for k, v in country_vectors.items()}
countries = list(country_case_vectors.keys())

if len(countries) < 2:
    print("Not enough countries to compute cosine similarity.")
    sys.exit(0)

# Obliczanie podobieństwa kosinusowego dla każdej pary krajów
results = []
for country_a, country_b in combinations(countries, 2):  # Generowanie par krajów
    similarity = cosine_similarity(
        country_case_vectors[country_a],
        country_case_vectors[country_b],
    )
    results.append((country_a, country_b, similarity))

# Sortowanie wyników alfabetycznie pod względem nazw krajów
results.sort(key=lambda x: (x[0], x[1]))

# Wyświetlenie wyników w formacie `kraj_a - kraj_b: similarity`
for country_a, country_b, similarity in results:
    print(f"{country_a} - {country_b}\t{similarity:.4f}")
