from models.translator import Translator

# CSV to JSON
Translator.csv_to_json('data/csv/draftkings.csv', 'data/json/draftkings.json')

# CSV to Python Dicts
for item in Translator.csv_to_dicts('data/csv/draftkings.csv'):
    print(item)
