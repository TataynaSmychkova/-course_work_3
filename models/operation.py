from datetime import datetime


class Operation:
    def __init__(self):
        self.operations_list = []

    def get_executed_operations(self, data):
        """
        Вывод всех выполненных операций (EXECUTED).
        :param data:
        """
        for operation in data:
            if operation.get("state") == "EXECUTED":
                self.operations_list.append(operation)

    def get_sorted_executed_operations(self):
        """
        Вывод всех выполненных операций (EXECUTED) по дате
        начиная с самой последней.
        """
        self.operations_list = sorted(self.operations_list, key=lambda operation: operation["date"], reverse=True)

    def get_last_five_operations(self):
        """
        Вывод 5 последних выполненных операций (EXECUTED).
        """
        self.operations_list = self.operations_list[:5]

    def change_format_date(self):
        """
        Изменение формата даты
        """
        for operation in self.operations_list:
            date = operation["date"]
            new_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
            operation["date"] = new_date.strftime("%d.%m.%Y")

    def hide_account(self):
        """
        Кодировка номеров карт и счетов.
        """
        for operation in self.operations_list:
            if operation["to"].startswith("Счет"):
                operation["to"] = operation["to"].split()[0] + " **" + operation["to"][-4:]
            else:
                card_new = operation["to"].split()
                card = card_new.pop()
                card1 = card[:4] + " " + card[4:6] + "** **** " + card[-4:]
                card_new.append(card1)
                operation["to"] = " ".join(card_new)
            if operation.get("from"):
                if operation["from"].startswith("Счет"):
                    operation["from"] = operation["from"].split()[0] + " **" + operation["from"][-4:]
                else:
                    card_new = operation["from"].split()
                    card = card_new.pop()
                    card1 = card[:4] + " " + card[4:6] + "** **** " + card[-4:]
                    card_new.append(card1)
                    operation["from"] = " ".join(card_new)

    def get_result(self, data):
        """
        Вывод пяти последних операции:
        :param data:
        """
        for operation in self.operations_list:
            print(operation["date"], operation["description"])
            print(operation.get("from", ""), "->", operation["to"])
            print(operation["operationAmount"]["amount"], operation["operationAmount"]["currency"]["name"])
            print()
