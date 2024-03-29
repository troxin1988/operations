from operations.utils import read_json

from os import path

path_to_json = path.join("operations", "operations.json")


def test_read_json():
    assert type(read_json(path_to_json)) == list
    assert read_json("") == None
