def filter_by_state(raw_state_data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """принимает список словарей и возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""
    if not isinstance(state, str):
        raise TypeError("Введите значение ключа")
    return [key for key in raw_state_data if key.get("state") == state]


def sort_by_date(raw_date_data: list[dict], reverse: bool = True) -> list[dict]:
    """принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (date)"""

    return sorted(raw_date_data, key=lambda key: key["date"], reverse=reverse)


check = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]

