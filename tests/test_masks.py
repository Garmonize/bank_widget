import pytest

from src.masks import get_mask_account_number, get_mask_card_number


def test_get_mask_card_number_with_fixtures(input_card_number_fix: str, result_card_number_fix: str) -> None:
    """функция проверяет правильность маскировки номера карты"""
    assert get_mask_card_number(input_card_number_fix) == result_card_number_fix


@pytest.mark.parametrize(
    "input_card_number, expected_card_number",
    [
        ("5674746564736453", "5674 74** **** 6453"),
        ("1234123412341234", "1234 12** **** 1234"),
    ],
)
def test_get_mask_card_number(input_card_number: str, expected_card_number: str) -> None:
    """функция проверяет правильность маскировки номера карты"""
    assert get_mask_card_number(input_card_number) == expected_card_number


@pytest.mark.parametrize(
    "wrong_card_number",
    [
        None,
        "728473287587540238475093827540875",
        "78364",
        "ajhsvbf897198709871234",
    ],
)
def test_get_mask_card_number_error(wrong_card_number: str) -> None:
    """функция проверяет вывод ошибки при вводе пользователем данных карты не в правильном формате"""
    with pytest.raises(ValueError) as exc_card_info:
        get_mask_card_number(wrong_card_number)

    assert str(exc_card_info.value) == "Введите корректный номер карты. Номер должен состоять из 16 цифр, без пробелов"


def test_get_mask_account_number_with_fixtures(
    input_account_number_fix: str, result_account_card_number_fix: str
) -> None:
    """функция проверяет правильность маскировки номера счета"""
    assert get_mask_account_number(input_account_number_fix) == result_account_card_number_fix


@pytest.mark.parametrize(
    "input_account_number, expected_account_number",
    [("73654108430135874305", "**4305"), ("76172634987162398476", "**8476")],
)
def test_get_mask_account_number(input_account_number: str, expected_account_number: str) -> None:
    """функция проверяет правильность маскировки номера счета"""
    assert get_mask_account_number(input_account_number) == expected_account_number


@pytest.mark.parametrize(
    "wrong_account_number",
    [
        None,
        "87687697869889718972458787147",
        "981724",
        "huijkb1249809843",
    ],
)
def test_get_mask_account_number_error(wrong_account_number: str) -> None:
    """функция проверяет вывод ошибки при вводе пользователем данных счета не в правильном формате"""
    with pytest.raises(ValueError) as exc_account_info:
        get_mask_account_number(wrong_account_number)

    assert (
        str(exc_account_info.value) == "Введите корректный номер счета. Номер должен состоять из 20 цифр, без пробелов"
    )
