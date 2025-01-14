from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: str) -> str:
    """Функция принимает строку содержащую тип карты, ее номер или счет и возвращает строку с замаскированным счетом
    в формате Visa Platinum 7000 79** **** 6361 или Счет **4305"""
    formatted = card_info.split(" ")  # создается список из строки, разделенный пробелами
    if "Счет" in formatted:
        masked_account_number = get_mask_account(formatted[1])
        return f"{formatted[0]} {masked_account_number}"
    elif len(formatted) > 2:
        masked_card_number = get_mask_card_number(formatted[2])
        return f"{formatted[0]} {formatted[1]} {masked_card_number}"
    else:
        masked_card_number = get_mask_card_number(formatted[1])
        return f"{formatted[0]} {masked_card_number}"


def get_date(date_data: str) -> str:
    """Функция принимает строку с необработанной датой, очищает ее и возвращает строку в формате ДД.ММ.ГГГГ"""
    cleaned_str = date_data.split("T")[0]  # разделяет строку по символу Т и выводит только первый индекс
    year, month, day = cleaned_str.split("-")  # разделяет значение по символу "-" и добавляются переменные
    formatted_date = f"{day}.{month}.{year}"
    return formatted_date


print(mask_account_card(input()))
print(get_date(input()))
