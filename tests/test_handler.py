import pytest

from operations.classes.handler import Handler

operations = [
    {"id": 1, "state": "EXECUTED", "date": "2018-01-01T00:00:00.000000"},
    {"id": 2, "state": "CANCELED", "date": "2018-02-01T00:00:00.000000"},
    {"id": 3, "state": "EXECUTED", "date": "2018-03-01T00:00:00.000000"},
    {"id": 4, "state": "EXECUTED", "date": "2018-01-01T00:00:00.000001"}
]

operation1 = {
    "id": 360577236,
    "state": "EXECUTED",
    "date": "2019-09-07T07:20:13.889610",
    "operationAmount": {
        "amount": "18536.73",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод с карты на карту",
    "from": "Maestro 4284341727554246",
    "to": "МИР 1582474475547301"
}

formated_operation1 = ("\n07.09.2019 Перевод с карты на карту\n"
                       "Maestro 4284 34** **** 4246 -> МИР 1582 47** **** 7301\n"
                       "18536.73 руб.")

operation2 = {
    "id": 360577236,
    "state": "EXECUTED",
    "date": "2019-09-07T07:20:13.889610",
    "operationAmount": {
        "amount": "18536.73",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Открытие вклада",
    "to": "МИР 1582474475547301"
}

formated_operation2 = ("\n07.09.2019 Открытие вклада\n"
                       "МИР 1582 47** **** 7301\n"
                       "18536.73 руб.")


@pytest.fixture
def operations_fixture():
    return operations


def test_filter_operations(operations_fixture):
    assert len(Handler().filter_operations(operations_fixture)) == 3


def test_sort_operations(operations_fixture):
    assert [i["id"] for i in Handler().sort_operations(operations_fixture)] == [3, 2, 4, 1]


def test_format_account():
    assert Handler().format_account("Visa Classic 7756673469642839") == "Visa Classic 7756 67** **** 2839"
    assert Handler().format_account("Maestro 7756673469642839") == "Maestro 7756 67** **** 2839"
    assert Handler().format_account("Счет 7756673469642839") == "Счет **2839"


def test_format_operation():
    assert Handler().format_operation(operation1) == formated_operation1
    assert Handler().format_operation(operation2) == formated_operation2
