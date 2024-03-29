import json


def read_json(filename: str) -> list | None:
    """
    Функция читает файл json.
    :param filename: Путь к файлу
    :return: Список словарей, если файл найден, иначе None
    """
    try:
        with open(filename, "r", encoding="UTF-8") as file:
            all_operations = json.load(file)
    except FileNotFoundError:
        print("File not found")
        return None
    return all_operations
