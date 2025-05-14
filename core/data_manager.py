import json

def load_car_data(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)
