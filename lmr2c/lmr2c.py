import csv

def load_population_data(filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        return {row[0].strip(): int(row[1].strip()) for row in reader if len(row) == 2 and row[1].isdigit()}

def load_vaccination_data(filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        data = {}
        for row in reader:
            if len(row) < 4:
                continue
            country = row[1].strip()
            try:
                cumulative_vaccinated = int(row[3].strip())
            except ValueError:
                continue
            if country not in data or cumulative_vaccinated > data[country]:
                data[country] = cumulative_vaccinated
        return data

def calculate_and_save(pop_dict, vacc_dict, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for country in sorted(vacc_dict.keys()):
            vaccinated = vacc_dict[country]
            population = pop_dict.get(country)
            if population and 0 < vaccinated < population:
                percent = (vaccinated / population) * 100
                f.write(f"{country}\t{percent:.2f}%\n")

population_file = "populations.csv"
vaccination_file = "vaccinated.csv"
output_file = "output.txt"

population_data = load_population_data(population_file)
vaccination_data = load_vaccination_data(vaccination_file)
calculate_and_save(population_data, vaccination_data, output_file)
