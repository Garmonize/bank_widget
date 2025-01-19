import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state",
    [
        "EXECUTED",
    ]
)
def test_state_filtration(input_raw_data_to_be_filtered: list[dict], result_raw_data_to_be_filtered: list[dict], state: str,) -> None:
    assert filter_by_state(input_raw_data_to_be_filtered, state) == result_raw_data_to_be_filtered



@pytest.mark.parametrize(
    "state",
    [
        (34),
    ]
)
def test_state_filtration(input_raw_data_to_be_filtered: list[dict], state: str,) -> None:
    with pytest.raises(TypeError) as exp_info:
        filter_by_state(input_raw_data_to_be_filtered, state)

    assert str(exp_info.value) == "Введите значение ключа"

@pytest.mark.parametrize(
    "reverse",
    [
        (True)
    ]

)
def test_sorting_by_date(input_raw_data_to_be_filtered: list[dict], result_sorting_by_date_reverse: list[dict], reverse: bool) -> None:
    assert sort_by_date(input_raw_data_to_be_filtered, reverse) == result_sorting_by_date_reverse

@pytest.mark.parametrize(
    "reverse",
    [
        (False)
    ]

)
def test_sorting_by_date(input_raw_data_to_be_filtered: list[dict], result_sorting_by_date_forward: list[dict], reverse: bool) -> None:
    assert sort_by_date(input_raw_data_to_be_filtered, reverse) == result_sorting_by_date_forward
