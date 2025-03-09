from xmlrpc.client import Fault

from utils.date_utils import transform_date, date_difference
import pytest


def test_date_input():
    day, month, year = transform_date("12/02/2022", "/")
    assert day == 12 and month == 2 and year == 2022


@pytest.mark.parametrize('actual_result, expected_result', [
    (date_difference((1, 12, 2024), (1, 2, 2025)), True),
    (date_difference((1, 12, 2025), (1, 2, 2013)), False),
    (date_difference((1, 1, 2024), (1, 2, 2024)), True),
    (date_difference((1, 1, 2024), (1, 5, 2024)), False),
])
def test_date_difference(actual_result, expected_result):
    assert actual_result == expected_result, f'Expected {expected_result}, but got {actual_result}'
