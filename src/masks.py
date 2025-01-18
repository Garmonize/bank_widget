def get_mask_card_number(card_number: str) -> str:
    """Функция get_mask_card_number принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX, где X — это цифра номера
    """
    if not isinstance(card_number, str) or not card_number.isdigit() or not len(card_number) == 16:
        raise TypeError("Введите корректный номер карты. Номер должен состоять из 16 цифр, без пробелов")

    formatted_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return formatted_card_number


def get_mask_account_number(account_number: str) -> str:
    """Функция get_mask_account принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера.
    """
    if not isinstance(account_number, str) or not account_number.isdigit() or not len(account_number) == 20:
        raise TypeError("Введите корректный номер счета. Номер должен быть состоять из 20 цифр, без пробелов")

    formatted_account_number = f"**{account_number[-4:]}"
    return formatted_account_number
