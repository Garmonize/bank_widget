from typing import Iterator

default_transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 123456789,
        "state": "PENDING",
        "date": "2021-07-15T15:10:20.101010",
        "operationAmount": {"amount": "4500.50", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Оплата услуг",
        "from": "Счет 12345678901234567890",
        "to": "Счет 09876543210987654321",
    },
    {
        "id": 987654321,
        "state": "CANCELED",
        "date": "2020-11-11T11:11:11.111111",
        "operationAmount": {"amount": "100.00", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Возврат средств",
        "from": "Счет 11223344556677889900",
        "to": "Счет 22334455667788990011",
    },
    {
        "id": 555555555,
        "state": "EXECUTED",
        "date": "2023-03-22T22:22:22.222222",
        "operationAmount": {"amount": "12345.67", "currency": {"name": "USD", "code": "USD"}},
        "description": "Пополнение счета",
        "from": "Счет 99887766554433221100",
        "to": "Счет 11223344556677889900",
    },
]


def filter_by_currency(transaction_for_filter: list[dict], currency: str = "USD") -> Iterator[dict]:
    """Принимает на вход список словарей представляющих транзакции и итератор, который поочередно выдает
    транзакции, где валюта операции соответствует заданной"""
    if not isinstance(transaction_for_filter, list):
        raise TypeError("Данные переданы неверно")
    return (x for x in transaction_for_filter if x["operationAmount"]["currency"]["code"] == currency.upper())


filtered_data = filter_by_currency(default_transactions)
while True:
    try:
        print(next(filtered_data))
    except StopIteration:
        break


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction.get("description", "No description")


descriptions = transaction_descriptions(default_transactions)
while True:
    try:
        print(next(descriptions))
    except StopIteration:
        break


REG_LENGHT = 16


def card_number_generator(beginning: int = 1, end: int = 9999999999999999) -> Iterator[str]:
    """функция генерирует значения карт от 1 до 9999 9999 9999 9999, принимая начальное и конечное значения, а также,
    если они не заданы, то генерирует по значениям по умолчанию. Функция также приводит полученные номера карт к
    банковскому формату ХХХХ ХХХХ ХХХХ ХХХХ"""
    for number in range(beginning, end + 1):
        number_str = str(number)
        number_len = len(number_str)
        if number_len < REG_LENGHT:
            number_str = "0" * (REG_LENGHT - number_len) + number_str
        grouped_bank_number = " ".join(number_str[i : i + 4] for i in range(0, REG_LENGHT, 4))
        yield grouped_bank_number


card_number = card_number_generator()
print(next(card_number))
