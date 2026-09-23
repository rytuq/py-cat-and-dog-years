import pytest

from app.main import get_human_age


def test_zero_age():
    assert get_human_age(0, 0) == [0, 0]


def test_below_first_threshold():
    assert get_human_age(14, 14) == [0, 0]


def test_at_first_threshold():
    assert get_human_age(15, 15) == [1, 1]


def test_before_second_threshold():
    assert get_human_age(23, 23) == [1, 1]


def test_at_second_threshold():
    assert get_human_age(24, 24) == [2, 2]


def test_before_next_cat_dog_step():
    assert get_human_age(27, 27) == [2, 2]


def test_cat_extra_step_dog_not_yet():
    assert get_human_age(28, 28) == [3, 2]


def test_dog_extra_step():
    assert get_human_age(28, 29) == [3, 3]


def test_large_age():
    assert get_human_age(100, 100) == [21, 17]


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (1, 1, [0, 0]),
        (14, 14, [0, 0]),
        (15, 0, [1, 0]),
        (0, 15, [0, 1]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (31, 32, [3, 3]),
        (32, 33, [4, 3]),
        (100, 100, [21, 17]),
    ],
)
def test_parametrized(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected
