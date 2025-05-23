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

for line in sys.stdin:
    line = line.strip()
    try:
        country, cases, timestamp = line.split('\t')
        cases = int(cases)
        timestamp = int(timestamp)
        country_vectors[country].append((timestamp, cases))
    except ValueError:
        continue

sorted_data = []
for country, values in country_vectors.items():
    for timestamp, cases in values:
        sorted_data.append((timestamp, country, cases))
sorted_data.sort()

sorted_country_vectors = defaultdict(list)
for _, country, cases in sorted_data:
    sorted_country_vectors[country].append(cases)

countries = list(sorted_country_vectors.keys())
if len(countries) < 2:
    print("Not enough countries to compute cosine similarity.")
    sys.exit(0)

results = []
for country_a, country_b in combinations(countries, 2):
    similarity = cosine_similarity(
        sorted_country_vectors[country_a],
        sorted_country_vectors[country_b],
    )
    results.append((country_a, country_b, similarity))

results.sort(key=lambda x: (x[0], x[1]))

for country_a, country_b, similarity in results:
    print(f"{country_a} - {country_b}\t{similarity:.4f}")
