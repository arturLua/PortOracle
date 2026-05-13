import json

def save_results(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)