import pytest

from src.widget import mask_account_card


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
def test_wrong_data_input(wrong_number_input: str) -> None:
    with pytest.raises(TypeError) as exc_info:
        mask_account_card(wrong_number_input)

    assert str(exc_info.value) == "Введите корректные данные"
