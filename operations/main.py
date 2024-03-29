import os
from utils import read_json, filter_operations, sort_operations, format_operation

def main():
    path = os.path.join("operations.json")
    operations = read_json(path)
    operations = filter_operations(operations)
    operations = sort_operations(operations)
    for operation in operations[:5]:
        print(format_operation(operation))


if __name__ == "__main__":
    main()