from datetime import datetime


class Handler:
    def filter_operations(self, operations: list) -> list:
        """
        Возвращает операции, которые EXECUTE.

        :param operations: список операций
        :return: список отфильтрованных операций
        """

        filtered = list(filter(lambda x: x.get("state") == "EXECUTED", operations))
        return filtered

    def sort_operations(self, operations: list) -> list:
        """
        Сортирует операции по дате (по убыванию)

        :param operations: список операций
        :return: Отсортированный список
        """

        sorted_operations = sorted(operations,
                                   key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"),
                                   reverse=True)
        return sorted_operations

    def format_account(self, account: str) -> str:
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

    def format_operation(self, operation: dict) -> str:
        """
        Преобразует операцию в форматированную строку вида:
        14.10.2018 Перевод организации
        Visa Platinum 7000 79** **** 6361 -> Счет **9638
        82771.72 руб.
        """

        datetime_obj = datetime.strptime(operation["date"], "%Y-%m-%dT%H:%M:%S.%f")
        op_date = datetime.strftime(datetime_obj, "%d.%m.%Y")
        op_description = operation["description"]
        if op_description.lower() != "открытие вклада":
            op_from = self.format_account(operation["from"]) + " -> "
        else:
            op_from = ""
        op_to = self.format_account(operation["to"])
        op_amount = operation["operationAmount"]["amount"]
        op_currency = operation["operationAmount"]["currency"]["name"]

        result = (f"\n{op_date} {op_description}\n"
                  f"{op_from}{op_to}\n"
                  f"{op_amount} {op_currency}")

        return result

    def execute(self, operations, number):
        operations = self.filter_operations(operations)
        operations = self.sort_operations(operations)
        for operation in operations[:number]:
            print(self.format_operation(operation))
