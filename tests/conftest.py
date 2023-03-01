import pytest
from models.operation import Operation


@pytest.fixture()
def verification_data():
    return [
        {
            "id": 147815167,
            "state": "CANCELED",
            "date": "2018-01-26T15:40:13.413061",
            "operationAmount": {
                "amount": "50870.71",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 4598300720424501",
            "to": "Счет 43597928997568165086"
        },
        {
            "id": 518707726,
            "state": "EXECUTED",
            "date": "2018-11-29T07:18:23.941293",
            "operationAmount": {
                "amount": "3348.98",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "MasterCard 3152479541115065",
            "to": "Visa Gold 9447344650495960"
        },
        {
            "id": 649467725,
            "state": "EXECUTED",
            "date": "2018-04-14T19:35:28.978265",
            "operationAmount": {
                "amount": "96995.73",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 27248529432547658655",
            "to": "Счет 97584898735659638967"
        },
        {
            "id": 782295999,
            "state": "EXECUTED",
            "date": "2019-09-11T17:30:34.445824",
            "operationAmount": {
                "amount": "54280.01",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 24763316288121894080",
            "to": "Счет 96291777776753236930"
        },
        {
            "id": 542678139,
            "state": "EXECUTED",
            "date": "2018-10-14T22:27:25.205631",
            "operationAmount": {
                "amount": "90582.51",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 2256483756542539",
            "to": "Счет 78808375133947439319"
        },
        {
            "id": 801684332,
            "state": "EXECUTED",
            "date": "2019-11-05T12:04:13.781725",
            "operationAmount": {
                "amount": "21344.35",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 77613226829885488381"
        },
        {
            "id": 122284694,
            "state": "EXECUTED",
            "date": "2019-08-08T21:58:06.688541",
            "operationAmount": {
                "amount": "98657.83",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 99668626339273709694",
            "to": "Счет 27219929444683698245"
        }
    ]


@pytest.fixture()
def operation(verification_data):
    operation = Operation()
    operation.get_executed_operations(verification_data)
    return operation
