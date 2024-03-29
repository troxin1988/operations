import pytest

from operations.utils import read_json, filter_operations, sort_operations
from os import path

operations = [
    {"id": 1, "state": "EXECUTED", "date": "2018-01-01T00:00:00.000000"},
    {"id": 2, "state": "CANCELED", "date": "2018-02-01T00:00:00.000000"},
    {"id": 3, "state": "EXECUTED", "date": "2018-03-01T00:00:00.000000"},
    {"id": 4, "state": "EXECUTED", "date": "2018-01-01T00:00:00.000001"}
]


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
