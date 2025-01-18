import pytest


@pytest.fixture
def input_card_number_fix() -> str:
    return "5674746564736453"


@pytest.fixture
def result_card_number_fix() -> str:
    return "5674 74** **** 6453"
