import json
from datetime import datetime


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


def filter_operations(operations: list) -> list:
    """
    Возвращает операции, которые EXECUTE.

    :param operations: список операций
    :return: список отфильтрованных операций
    """

    filtered = list(filter(lambda x: x.get("state") == "EXECUTED", operations))
    return filtered


def sort_operations(operations: list) -> list:
    """
    Сортирует операции по дате (по убыванию)

    :param operations: список операций
    :return: Отсортированный список
    """

    sorted_operations = sorted(operations,
                               key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"),
                               reverse=True)
    return sorted_operations
