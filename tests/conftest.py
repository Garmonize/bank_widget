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
