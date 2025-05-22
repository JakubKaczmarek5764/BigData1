#!/usr/bin/python3.12

import csv
from functools import reduce
from math import sqrt
from itertools import combinations
from collections import defaultdict

def cosine_similarity(vecA, vecB):
    dot_product = sum(a * b for a, b in zip(vecA, vecB))
    magnitude_a = sqrt(sum(a * a for a in vecA))
    magnitude_b = sqrt(sum(b * b for b in vecB))
    if magnitude_a == 0 or magnitude_b == 0:
        return 0
    return dot_product / (magnitude_a * magnitude_b)

def parse_line(line):
    try:
        if not line or line.startswith(',country') or line.strip() == '':
            return None
        
        parts = line.strip().split(',')
        if len(parts) < 5:
            return None
            
        country = parts[1]
        cases_str = parts[2]
        timestamp_str = parts[4]

        if not cases_str.isdigit() or not timestamp_str.isdigit():
            return None
            
        cases = int(cases_str)
        timestamp = int(timestamp_str)
        
        return (country, cases, timestamp)
    except (ValueError, IndexError):
        return None

def group_by_country(acc, item):
    if item is None:
        return acc
    
    country, cases, timestamp = item
    if country not in acc:
        acc[country] = []
    acc[country].append((cases, timestamp))
    return acc

def process_country_data(country_data):
    country, data_list = country_data
    sorted_data = sorted(data_list, key=lambda x: x[1])
    cases_vector = [cases for cases, timestamp in sorted_data]
    return (country, cases_vector)

def calculate_similarities(country_vectors):
    countries = list(country_vectors.keys())
    
    if len(countries) < 2:
        print("Not enough countries to compute cosine similarity.")
        return []
    
    results = []
    for country_a, country_b in combinations(countries, 2):
        similarity = cosine_similarity(
            country_vectors[country_a],
            country_vectors[country_b]
        )
        results.append((country_a, country_b, similarity))

    results.sort(key=lambda x: (x[0], x[1]))
    return results

def main():
    filename = 'confirmed_deceased.csv'
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        parsed_data = list(map(parse_line, lines))

        valid_data = list(filter(lambda x: x is not None, parsed_data))

        country_grouped = reduce(group_by_country, valid_data, defaultdict(list))

        country_vectors_list = list(map(process_country_data, country_grouped.items()))

        country_vectors = dict(country_vectors_list)

        results = calculate_similarities(country_vectors)

        output_filename = 'cosine_similarities.txt'
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            for country_a, country_b, similarity in results:
                output_file.write(f"{country_a} - {country_b} {similarity:.4f}\n")
        
        print(f"Results saved to '{output_filename}'")
        print(f"Total pairs processed: {len(results)}")

        if results:
            print("\nPreview of results:")
            for country_a, country_b, similarity in results[:5]:
                print(f"{country_a} - {country_b} {similarity:.4f}")
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    main()