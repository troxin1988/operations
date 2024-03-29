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


def format_account(account: str) -> str:
    """
    Форматирует номер счета или карты, приводя его к шаблонам:
    - Visa Platinum 7000 79** **** 6361
    - Счет **9638

    :param account: счет или карта
    :return: форматированная строка
    """

    *type_account, number = account.split()
    type_account = " ".join(type_account)
    if type_account.lower() == "счет":
        # последние 4 цифры счета, установив ** перед ними
        number = number[-4:].rjust(6, "*")
    else:
        # разбивка на 4 блока, редактирование и слияние
        number = [number[block * 4:block * 4 + 4] for block in range(4)]
        number[1] = number[1][:2].ljust(4, "*")
        number[2] = "*" * 4
        number = " ".join(number)

    return " ".join((type_account, number))
