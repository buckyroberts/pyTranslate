import csv
import json

csv_file = open('data/people.csv', 'r')
json_file = open('data/people.json', 'w')
field_names = set()
results = []


with open('data/people.csv') as f:
    csv_data = csv.DictReader(csv_file, next(csv.reader(f)))
    next(csv_data)
    for row in csv_data:
        results.append(row)
    json.dump(results, json_file)
