from models.data import Data
from settings import OPERATION_PATH
from models.operation import Operation
from models.data import Data


def test_get_data():
    data = Data(OPERATION_PATH).get_data()
    assert isinstance(data, list)
    assert isinstance(data[0], dict)


def test_get_executed_operations(operation):
    assert len(operation.operations_list) == 6


def test_get_sorted_executed_operations(operation):
    operation.get_sorted_executed_operations()
    assert operation.operations_list[0]["id"] == 801684332


def test_get_last_five_operations(operation):
    operation.get_last_five_operations()
    assert len(operation.operations_list) == 5


def test_change_format_date(operation):
    operation.change_format_date()
    assert operation.operations_list[0]["date"] == "29.11.2018"


def test_hide_account(operation):
    operation.hide_account()
    assert operation.operations_list[0]


