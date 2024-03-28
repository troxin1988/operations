import json


def read_json(filename: str) -> list | None:
    try:
        with open(filename, "r", encoding="UTF-8") as file:
            all_operations = json.load(file)
    except FileNotFoundError:
        print("File not found")
        return None
    return all_operations
