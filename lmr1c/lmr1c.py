import csv
from functools import reduce
from collections import defaultdict

with open("dane.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # pomiń nagłówek

    filtered_rows = filter(
        lambda row: len(row) >= 3 and row[1].strip() and row[2].isdigit(),
        reader
    )

    mapped = map(lambda row: (row[1].strip(), int(row[2].strip())), filtered_rows)

    def reducer(acc, pair):
        country, cases = pair
        acc[country] += cases
        return acc

    result = reduce(reducer, mapped, defaultdict(int))

with open("output.txt", "w", encoding="utf-8") as f:
    for country, total_cases in sorted(result.items()):
        f.write(f"{country}\t{total_cases}\n")
