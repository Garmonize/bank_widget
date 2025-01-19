import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_card_or_account_number, expected_masked_card_or_account_number",
    [
        ("VISA GOLD 1234567890123456", "Visa Gold 1234 56** **** 3456"),
        ("VISA PLATINUM 0987654321098765", "Visa Platinum 0987 65** **** 8765"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Mastercard 5437465747382938", "MasterCard 5437 46** **** 2938"),
        ("Счет 12345123451234512345", "Счет **2345"),
    ],
)
def test_mask_account_type(input_card_or_account_number: str, expected_masked_card_or_account_number: str) -> None:
    """функция тестирует корректность значении при вводе данных"""
    assert mask_account_card(input_card_or_account_number) == expected_masked_card_or_account_number


@pytest.mark.parametrize(
    "uncleaned_format, cleaned_format",
    [
        ("VISA PLATINUM 1234-5678-9012-3456", "Visa Platinum 1234 56** **** 3456"),
        ("VISAPLATINUM1234567890123456", "Visa Platinum 1234 56** **** 3456"),
        ("VISA PLATINUM 1234/5678/9012/3456", "Visa Platinum 1234 56** **** 3456"),
        ("VISA PLATINUM1234-5678-9012-3456", "Visa Platinum 1234 56** **** 3456"),
        ("1234-5678-9012-3456VISA PLATINUM", "Visa Platinum 1234 56** **** 3456"),
        ("1234-5678-9012-3456VISAPLATINUM", "Visa Platinum 1234 56** **** 3456"),
        ("1234-5678-9012-3456 VISAPLATINUM", "Visa Platinum 1234 56** **** 3456"),
        ("1234123412341234", "1234 12** **** 1234"),
    ],
)
def test_uncleaned_format(uncleaned_format: str, cleaned_format: str) -> None:
    """функция тестирует форматирование ввода пользователя согласно заданным параметрам"""
    assert mask_account_card(uncleaned_format) == cleaned_format


@pytest.mark.parametrize(
    "wrong_number_input",
    [
        "виза голд 0843",
        "89723874",
        "897098739148509870987093184705897",
        "uywury817238740127340891778917203847kjhghwe",
    ],
)
def test_wrong_numbers_input(wrong_number_input: str) -> None:
    """функция тестирует появление ошибки, если данные были введены некорректно"""
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(wrong_number_input)

    assert str(exc_info.value) == "Введите корректные данные"


@pytest.mark.parametrize(
    "raw_date_input, expected_date_format",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-03-11T02:26:18", "11.03.2024"),
    ],
)
def test_get_formatted_date(raw_date_input: str, expected_date_format: str) -> None:
    """функция тестирует обработку данных с милисекундами и без"""
    assert get_date(raw_date_input) == expected_date_format


@pytest.mark.parametrize("wrong_date_input", ["2024809809[8411234", "date", "2"])
def test_wrong_date_format(wrong_date_input: str) -> None:
    """функция тестирует появление ошибки, если данные были введены некорректно"""
    with pytest.raises(ValueError) as exp_info:
        get_date(wrong_date_input)

    assert str(exp_info.value) == "Введите корректный формат даты"
