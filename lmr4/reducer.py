#!/usr/bin/python3.12
"""reducer.py"""

import sys
from collections import defaultdict
from math import sqrt

country_vectors = defaultdict(list)


def cosine_similarity(vecA, vecB):
    dot_product = sum(a * b for a, b in zip(vecA, vecB))
    magnitude_a = sqrt(sum(a * a for a in vecA))
    magnitude_b = sqrt(sum(b * b for b in vecB))
    if magnitude_a == 0 or magnitude_b == 0:
        return 0
    return dot_product / (magnitude_a * magnitude_b)


for line in sys.stdin:
    line = line.strip()
    country, cases = line.split('\t')
    cases = int(cases)
    country_vectors[country].append(cases)

countries = list(country_vectors.keys())
for i in range(len(countries)):
    country_a = countries[i]
    for j in range(i + 1, len(countries)):
        country_b = countries[j]
        similarity = cosine_similarity(country_vectors[country_a], country_vectors[country_b])
        print(f"{country_a} - {country_b}\t{similarity:.4f}")
