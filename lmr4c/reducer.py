#!/usr/bin/python3.12
"""reducer.py"""

import sys
from collections import defaultdict
from math import sqrt

# Funkcja obliczająca podobieństwo kosinusowe
def cosine_similarity(vecA, vecB):
    dot_product = sum(a * b for a, b in zip(vecA, vecB))
    magnitude_a = sqrt(sum(a * a for a in vecA))
    magnitude_b = sqrt(sum(b * b for b in vecB))
    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0  # Unikamy dzielenia przez zero
    return dot_product / (magnitude_a * magnitude_b)


# Przechowywanie danych w Reducerze
all_country_vectors = defaultdict(list)

# Wczytywanie danych z Combinerów
for line in sys.stdin:
    line = line.strip()
    country, cases_list_str = line.split('\t')
    cases_list = list(map(int, cases_list_str.split(',')))
    all_country_vectors[country].extend(cases_list)  # Łączenie list przypadków w całość

# Obliczanie podobieństw kosinusowych
countries = list(all_country_vectors.keys())
for i in range(len(countries)):
    country_a = countries[i]
    for j in range(i + 1, len(countries)):
        country_b = countries[j]
        similarity = cosine_similarity(all_country_vectors[country_a], all_country_vectors[country_b])
        print(f"{country_a} - {country_b}\t{similarity:.4f}")