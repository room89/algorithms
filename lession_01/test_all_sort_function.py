import random

import pytest

import sorting


def get_all_functions(module):
    return {name for name in dir(sorting) if not name.startswith('__')}


@pytest.mark.parametrize('function_name', get_all_functions(sorting))
def test_simple(function_name):
    function = getattr(sorting, function_name)
    assert function([1, 2, 3, 4, -1]) == [-1, 1, 2, 3, 4]


@pytest.mark.parametrize('function_name', get_all_functions(sorting))
def test_exceptions(function_name):
    function = getattr(sorting, function_name)
    with pytest.raises(TypeError):
        function([1, 'a'])


@pytest.mark.parametrize('array', [
    [1, 23, 4, 51, 11, 21312, 312, 44.1213, 21312],
    [x for x in range(100)],
    [x for x in range(100, 0, -1)],
])
@pytest.mark.parametrize('function_name', get_all_functions(sorting))
def test_random_cases(function_name, array):
    function = getattr(sorting, function_name)
    for i in range(100):
        assert function(array) == sorted(array)


@pytest.mark.parametrize('function_name', get_all_functions(sorting))
def test_strings(function_name):
    function = getattr(sorting, function_name)
    string = 'asdfafafa'
    assert function(string) == sorted(string)
