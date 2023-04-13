import datetime
import json
from datetime import datetime


def load_operations():
    """
    Функция load_operations, открытие файла.
    """
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def filter_data(data):
    """
    Функция filter_data, производит фильтрацию транзакций
    """
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    return data


def sorted_key(x):
    return x['date']


def sort_data(data):
    """
    Функция sort_data, сортирует транзакции по дате
    sorted: сортировка
    """
    data = sorted(data, key=sorted_key, reverse=True)
    return data[:5]


def format_data(data):
    """
    Функция format_data, определяет формат
    :param data: формат даты
    :return: formatted_data собирает все в необходимый вид
    """
    formatted_data = []

    # amount = data['operationAmount']['amount']
    # currency_name = data['operationAmount']['currency']['name']

    for row in data:
        date = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime("%d.%m.%Y")
        description = row["description"]
        amount = row['operationAmount']['amount']
        currency = row['operationAmount']['currency']['name']
        if "from" in row:
            from_arrow = "->"
            sender = row['from'].split()
            sender_bill = sender.pop(-1)
            sender_info = " ".join(sender)
            sender_bill = f"{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}"
        else:
            sender_info = "Новый счет"
            sender_bill = ""
            from_arrow = ""

        if "to" in row:
            sender_to = row['to'].split()
            sender_bill_to = sender_to.pop(-1)
            sender_info_to = " ".join(sender_to)
            sender_bill_to = f"{sender_bill_to[:4]} {sender_bill_to[4:6]}** **** {sender_bill_to[-4:]}"
        else:
            sender_info_to = "Новый счет"
            sender_bill_to = ""





        formatted_data.append(f"""
{date} {description}
{sender_info} {sender_bill} {from_arrow}  {sender_info_to} {sender_bill_to}
{amount} {currency}
        """)
    return formatted_data
