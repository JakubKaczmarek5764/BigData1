import csv
from functools import reduce

def load_population_data(filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        filtered = filter(lambda row: len(row) == 2 and row[1].isdigit(), reader)
        mapped = map(lambda row: (row[0].strip(), int(row[1].strip())), filtered)
        return dict(mapped)

def load_vaccination_data(filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        def reducer(acc, row):
            if len(row) < 4:
                return acc
            country = row[1].strip()
            try:
                vaccinated = int(row[3].strip())
            except ValueError:
                return acc
            if country not in acc or vaccinated > acc[country]:
                acc[country] = vaccinated
            return acc

        return reduce(reducer, reader, {})

def calculate_and_save(pop_dict, vacc_dict, output_file):
    valid_data = filter(
        lambda item: item[0] in pop_dict and 0 < item[1] < pop_dict[item[0]],
        vacc_dict.items()
    )

    percentage_data = map(
        lambda item: (item[0], (item[1] / pop_dict[item[0]]) * 100),
        valid_data
    )

    sorted_data = sorted(percentage_data, key=lambda x: x[0])

    with open(output_file, 'w', encoding='utf-8') as f:
        for country, percent in sorted_data:
            f.write(f"{country}\t{percent:.2f}%\n")

population_file = "populations.csv"
vaccination_file = "vaccinated.csv"
output_file = "output.txt"

population_data = load_population_data(population_file)
vaccination_data = load_vaccination_data(vaccination_file)
calculate_and_save(population_data, vaccination_data, output_file)
