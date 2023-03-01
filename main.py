from models.data import Data
from models.operation import Operation
from settings import OPERATION_PATH


def main():
    data = Data(OPERATION_PATH).get_data()
    operation = Operation()
    operation.get_executed_operations(data)
    operation.get_sorted_executed_operations()
    operation.get_last_five_operations()
    operation.change_format_date()
    operation.hide_account()
    operation.get_result(data)


if __name__ == "__main__":
    main()
