import pytest

from operations.utils import read_json, filter_operations, sort_operations, format_account, format_operation
from os import path

operations = [
    {"id": 1, "state": "EXECUTED", "date": "2018-01-01T00:00:00.000000"},
    {"id": 2, "state": "CANCELED", "date": "2018-02-01T00:00:00.000000"},
    {"id": 3, "state": "EXECUTED", "date": "2018-03-01T00:00:00.000000"},
    {"id": 4, "state": "EXECUTED", "date": "2018-01-01T00:00:00.000001"}
]

operation = {
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

formated_operation = ("\n07.09.2019 Перевод с карты на карту\n"
                      "Maestro 4284 34** **** 4246 -> МИР 1582 47** **** 7301\n"
                      "18536.73 руб.")



@pytest.fixture
def operations_fixture():
    return operations


def test_read_json():
    path_to_json = path.join("operations", "operations.json")
    assert type(read_json(path_to_json)) == list
    assert read_json("") == None


def test_filter_operations(operations_fixture):
    assert len(filter_operations(operations_fixture)) == 3


def test_sort_operations(operations_fixture):
    assert [i["id"] for i in sort_operations(operations_fixture)] == [3, 2, 4, 1]


def test_format_account():
    assert format_account("Visa Classic 7756673469642839") == "Visa Classic 7756 67** **** 2839"
    assert format_account("Maestro 7756673469642839") == "Maestro 7756 67** **** 2839"
    assert format_account("Счет 7756673469642839") == "Счет **2839"


def test_format_operation():
    assert format_operation(operation) == formated_operation
