import random

import pytest
import numpy as np

import sorting


def test_simple():
    assert sorting.bubble_sort([1, 2, 3, 4, -1]) == [-1, 1, 2, 3, 4]


def test_exceptions():
    with pytest.raises(TypeError):
        sorting.bubble_sort([1, 'a'])


def generate_random_int_array(length=None, maximum=100):
    if not length:
        length = random.randint(0, 100)
    return list(np.random.randint(maximum, size=length))


def test_random_int_list():
    for i in range(100):
        array = generate_random_int_array()
        assert sorting.bubble_sort(array) == sorted(array)


def test_strings():
    string = 'asdfafafa'
    assert sorting.bubble_sort(string) == sorted(string)


def test_no_modify():
    arr = [4, 3, 2, 1]
    sorting.bubble_sort(arr)
    assert arr == [4, 3, 2, 1]


@pytest.mark.parametrize('array', [
    [1, 2, 3, 4],
    [2, 1, 3],
])
def test_strings(array):
    assert sorting.bubble_sort(array) == sorted(array)
