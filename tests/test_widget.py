# Функция
# mask_account_card
# :
# Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки в зависимости
# от типа входных данных (карта или счет).
# Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.
# Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам.
import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize(
    "input_card_or_account_number, expected_masked_card_or_account_number",
    [
        'VISA GOLD 1234567890123456', "VISA GOLD 1234 56** **** 3456"
    ]
)
def test_mask_account_type(input_card_or_account_number: str, expected_masked_card_or_account_number: str) -> None:
    assert mask_account_card(input_card_or_account_number) == expected_masked_card_or_account_number
