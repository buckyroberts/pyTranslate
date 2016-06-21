import csv
import json


class Translator:

    @staticmethod
    def csv_to_json(csv_file, json_file):
        results = []
        for row in csv.DictReader(open(csv_file, 'r')):
            results.append(row)
        json.dump(results, open(json_file, 'w'))
