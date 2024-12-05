import json

with open('values.json') as f:
    values = json.load(f)

with open('tests.json') as f:
    tests = json.load(f)

value_dict = {item['id']: item['value'] for item in values['values']}

def fill_values(test_data):
    if isinstance(test_data, dict):
        for key, value in test_data.items():
            if key == 'id' and value in value_dict:
                test_data['value'] = value_dict[value]
            elif isinstance(value, dict) or isinstance(value, list):
                fill_values(value)
    elif isinstance(test_data, list):
        for item in test_data:
            fill_values(item)

fill_values(tests)

with open('report.json', 'w') as f:
    json.dump(tests, f, indent=4)