from datetime import datetime

from src.masks import get_mask_account_number, get_mask_card_number


def mask_account_card(card_info: str) -> str:
    """Функция принимает строку содержащую тип карты, ее номер или счет и возвращает строку с замаскированным счетом
    в формате Visa Platinum 7000 79** **** 6361 или Счет **4305"""
    name_dict = {
        "visagold": "Visa Gold",
        "visaclassic": "Visa Classic",
        "visaplatinum": "Visa Platinum",
        "mastercard": "MasterCard",
        "maestro": "Maestro",
        "счет": "Счет",
    }
    raw_text = "".join([x for x in card_info if x.isalpha()])
    raw_digits = "".join([x for x in card_info if x.isdigit()])
    formatted_card_type = name_dict.get(raw_text.lower())
    if len(raw_digits) not in [16, 20]:
        raise TypeError("Введите корректные данные")
    elif len(raw_digits) == 16:
        return (
            f"{formatted_card_type if formatted_card_type is not None else ""} " 
            f"{get_mask_card_number(raw_digits)}").strip()
    else:
        return (
            f"{formatted_card_type if formatted_card_type is not None else ""} "
            f"{get_mask_account_number(raw_digits)}").strip()


def get_date(raw_date: str) -> str:
    """Функция принимает строку с необработанной датой, очищает ее и возвращает строку в формате ДД.ММ.ГГГГ"""
    date_obj = datetime.strptime(raw_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")
