def filter_by_state(raw_state_data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """принимает список словарей и возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""
    formatted_state_data = [key for key in raw_state_data if key.get("state") == state]

    return formatted_state_data


def sort_by_date(raw_date_data: list[dict], reverse: bool = True) -> list[dict]:
    """принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (date)"""

    return sorted(raw_date_data, key=lambda key: key["date"], reverse=reverse)
