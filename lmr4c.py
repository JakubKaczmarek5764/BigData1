import csv
from functools import reduce
from collections import defaultdict
from math import sqrt

def cosine_similarity(vecA, vecB):
    dot_product = sum(a * b for a, b in zip(vecA, vecB))
    magnitude_a = sqrt(sum(a * a for a in vecA))
    magnitude_b = sqrt(sum(b * b for b in vecB))
    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0
    return dot_product / (magnitude_a * magnitude_b)

# Wczytaj dane
country_cases = defaultdict(list)

with open("confirmed_deceased.csv", newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # pomiń nagłówek

    filtered = filter(lambda row: len(row) >= 3 and row[2].strip().isdigit(), reader)
    mapped = map(lambda row: (row[1].strip(), int(row[2].strip())), filtered)

    def reducer(acc, entry):
        country, confirmed = entry
        acc[country].append(confirmed)
        return acc

    country_cases = reduce(reducer, mapped, country_cases)

# Znajdź maksymalną długość
max_len = max(len(v) for v in country_cases.values())

# Uzupełnij zerami
for country in country_cases:
    country_cases[country] += [0] * (max_len - len(country_cases[country]))

# Oblicz i sortuj podobieństwa
countries = sorted(country_cases.keys())
similarity_results = []

for i in range(len(countries)):
    for j in range(i + 1, len(countries)):
        country1 = countries[i]
        country2 = countries[j]

        vec1 = country_cases[country1]
        vec2 = country_cases[country2]

        similarity = cosine_similarity(vec1, vec2)
        pair_key = f"{country1} - {country2}"
        similarity_results.append((pair_key, similarity))

# Sortuj po nazwie pary
similarity_results.sort(key=lambda x: x[0])

# Zapisz do pliku
with open("output.txt", "w", encoding="utf-8") as out:
    for pair, sim in similarity_results:
        out.write(f"{pair}\t{sim:.4f}\n")