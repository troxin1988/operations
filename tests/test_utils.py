from operations.utils import read_json, filter_operations
from os import path

operations = [
    {"state": "EXECUTED"},
    {"state": "CANCELED"},
    {},
    {"state": "EXECUTED"}
]


def test_read_json():
    path_to_json = path.join("operations", "operations.json")
    assert type(read_json(path_to_json)) == list
    assert read_json("") == None


def test_filter_operations():
    assert len(filter_operations(operations)) == 2
