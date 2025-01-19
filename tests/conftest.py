import pytest


@pytest.fixture
def input_card_number_fix() -> str:
    """функция возвращает заданный номер карты для использования его в качестве аргумента"""
    return "5674746564736453"


@pytest.fixture
def result_card_number_fix() -> str:
    """функция возвращает замаскированный номер карты для использования его в качестве аргумента"""
    return "5674 74** **** 6453"


@pytest.fixture
def input_account_number_fix() -> str:
    """функция возвращает заданный номер счета для использования его в качестве аргумента"""
    return "12345678901234567890"


@pytest.fixture
def result_account_card_number_fix() -> str:
    """функция возвращает замаскированный номер счета для использования его в качестве аргумента"""
    return "**7890"


@pytest.fixture
def input_raw_data_to_be_filtered() -> list[dict]:
    """функция возвращает сгенерированную коллекцию для проверки ввода"""
    stored_data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    return stored_data


@pytest.fixture
def result_raw_data_to_be_filtered() -> list[dict]:
    """функция возвращает сгенерированную коллекцию для проверки вывода с ключом по умолчанию"""
    result_stored_data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    return result_stored_data


@pytest.fixture
def result_sorting_by_date_reverse() -> list[dict]:
    """функция возвращает сгенерированную коллекцию для проверки вывода сортировки по дате по умолчанию убывание"""
    result_info = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    return result_info


@pytest.fixture
def result_sorting_by_date_forward() -> list[dict]:
    """функция возвращает сгенерированную коллекцию для проверки вывода сортировки по дате по возрастанию"""
    result_info = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    return result_info
