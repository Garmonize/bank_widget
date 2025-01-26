import pytest
from typing import Any

from src.generators import filter_by_currency


# написать тесты если:
# если все ровно,
# совсем нет данных,
# запрашиваемая валюта не найдена,
# не соблюден регистр
@pytest.mark.parametrize(
    "transactions, expected",
    [
        (
            [
                {
        "id": 555555555,
        "state": "EXECUTED",
        "date": "2023-03-22T22:22:22.222222",
        "operationAmount": {"amount": "12345.67", "currency": {"name": "USD", "code": "USD"}},
        "description": "Пополнение счета",
        "from": "Счет 99887766554433221100",
        "to": "Счет 11223344556677889900",
    }
            ],
[
    {
        "id": 555555555,
        "state": "EXECUTED",
        "date": "2023-03-22T22:22:22.222222",
        "operationAmount": {"amount": "12345.67", "currency": {"name": "USD", "code": "USD"}},
        "description": "Пополнение счета",
        "from": "Счет 99887766554433221100",
        "to": "Счет 11223344556677889900",
    }
]
        )
    ]
)
def test_filter_by_currency(transactions: list[dict], expected: list[dict]) -> None:
    """функция проверяет, что сортировка по валюте работает исправно"""
    result = list(filter_by_currency(transactions))
    assert result == expected


@pytest.mark.parametrize(
    "empty_input",
    [
        []
    ]
)
def test_no_data_was_set(empty_input: list) -> None:
    """функция проверяет, возвращается и строка с ошибкой, если не получено данных"""
    assert list(filter_by_currency(empty_input)) == []


@pytest.mark.parametrize(
    "wrong_input",
    [
        {},
        "ghjdthrf",
        1234,
        (),
    ]
)
def test_wrong_type_input(wrong_input: Any) -> None:
    """функция проверяет правильность работы при вводе других типов данных"""
    with pytest.raises(TypeError) as exp_info:
        filter_by_currency(wrong_input)

    assert str(exp_info.value) == "Данные переданы неверно"


def test_no_currensy_found():
    pass


def test_bad_register_entered():
    pass
