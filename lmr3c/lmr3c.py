import csv
from functools import reduce
from collections import defaultdict

aggregated = defaultdict(lambda: {"confirmed": 0, "deceased": 0})

with open("confirmed_deceased.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)

    filtered = filter(
        lambda row: len(row) >= 4 and row[1].strip() and row[2].isdigit() and row[3].isdigit(),
        reader
    )

    mapped = map(lambda row: (row[1].strip(), int(row[2]), int(row[3])), filtered)

    def reducer(acc, entry):
        country, confirmed, deceased = entry
        acc[country]["confirmed"] += confirmed
        acc[country]["deceased"] += deceased
        return acc

    aggregated = reduce(reducer, mapped, aggregated)

with open("output.txt", "w", encoding="utf-8") as f:
    for country, data in sorted(aggregated.items()):
        confirmed = data["confirmed"]
        deceased = data["deceased"]
        if confirmed > 0:
            death_rate = (deceased / confirmed) * 100
            f.write(f"{country}\t{death_rate:.2f}%\n")