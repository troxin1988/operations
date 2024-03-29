import os

from utils import read_json
from classes.handler import Handler


class Client:
    def __init__(self, name):
        self.name = name
        self.path = os.path.join("operations.json")
        self.handler = Handler()
        self.print_last_operations(5)

    def print_last_operations(self, number):
        operations = read_json(self.path)
        self.handler.execute(operations, number)
