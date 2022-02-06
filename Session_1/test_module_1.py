import pytest

from module_1 import *


def test_task_1_correct_work():
    numbers = []
    for i in range(1, 1001):
        if (i % 3 == 0) and (i % 5 == 0):
            numbers.append(i)

    output = task_1()

    assert output == numbers, (
        "Incorrect result"
    )


@pytest.mark.parametrize(
    'test_input, expected',
    [
        pytest.param("12Axda1303dad", (6, 7), id='Example: 12Axda1303dad'),
        pytest.param('0', (1, 0), id='Example: 0'),
        pytest.param('abrakadabra', (0, 11), id='Example: abrakadabra'),
        pytest.param('Data Engineering Lab is the best', (0, 27), id='Example: Data Engineering Lab is the best'),
        pytest.param('???', (0, 0), id='Example: ???'),
        pytest.param('', (0, 0), id='Example: '),
        pytest.param('  a1', (1, 1), id='Example:   a1'),
        pytest.param('11234', (5, 0), id='Example: 11234'),
    ],
)
def test_task_2_correct_work(test_input, expected):
    output = task_2(test_input)
    assert output == expected, (
        "See tests!"
    )


@pytest.mark.parametrize(
    'test_input_1, test_input_2, expected',
    [
        pytest.param(
            ["red", "orange", "green", "blue", "white"],
            ["black", "yellow", "green", "blue"],
            (['white', 'orange', 'red'], ['black', 'yellow']),
            id='Example: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]',
        ),
        pytest.param(
            ["Mike", "John", "Ann"],
            [12, "Egor", "Ann", "Jane"],
            (["Mike", "John"], [12, "Egor", "Jane"]),
            id='Example: ["Mike", "John", "Ann"], [12, "Egor", "Ann", "Jane"]',
        ),
        pytest.param(
            [5, 5, 5],
            [5, 5, 5],
            ([], [],),
            id='Example: [5, 5, 5], [5, 5, 5]',
        ),
        pytest.param(
            [1, 5, 5],
            [5, 1, 5],
            ([], [],),
            id='Example: [1, 5, 5], [5, 1, 5]',
        ),
        pytest.param(
            [1, 5, 4],
            [5, 1, 3],
            ([4], [3],),
            id='Example: [1, 5, 4], [5, 1, 3]',
        ),
        pytest.param(
            [1, 5, 4, 6],
            [5, 1, 4],
            ([6], [],),
            id='Example: [1, 5, 4, 6], [5, 1, 4]',
        ),
        pytest.param(
            [1, 5, 4, 6],
            [5, 1, 4],
            ([6], [],),
            id='Example: [1, 5, 4, 6], [5, 1, 4]',
        ),
        pytest.param(
            [1, 2, 3],
            [4, 5, 6],
            ([1, 2, 3], [4, 5, 6],),
            id='Example: [1, 2, 3], [4, 5, 6]',
        ),
    ],
)
def test_task_3_correct_work(test_input_1, test_input_2, expected):
    output = task_3(test_input_1, test_input_2)
    assert set(output[0]) == set(expected[0]), (
        "Incorrect first difference"
    )
    assert set(output[1]) == set(expected[1]), (
        "Incorrect second difference"
    )


@pytest.mark.parametrize(
    'test_input, expected',
    [
        pytest.param([11, 22, 33], 112233, id='Example: [11, 22, 33]'),
        pytest.param([0, 0], 0, id='Example: [0, 0]'),
        pytest.param([1], 1, id='Example: [1]'),
        pytest.param([999, 0], 9990, id='Example: [999, 0]'),
        pytest.param([999, 0, 10], 999010, id='Example: [999, 0, 10]'),
        pytest.param([0, 0, 999, 0, 10, 0], 9990100, id='Example: [0, 0, 999, 0, 10, 0]'),
        pytest.param([0, 0, 1, 0, 1], 101, id='Example: [0, 0, 999, 0, 10, 0]'),
    ],
)
def test_task_4_correct_work(test_input, expected):
    output = task_4(test_input)
    assert output == expected, (
        "See tests!"
    )


@pytest.mark.parametrize(
    'test_input, expected',
    [
        pytest.param([[11, 22, 33], [1, 2, 3]], [11, 22, 33], id='Example: [[11, 22, 33], [1,2,3]]'),
        pytest.param([[0, 0, 1], [0, 0, 2]], [0, 0, 2], id='Example: [[0, 0, 1], [0,0,2]]'),
        pytest.param([[0], [0]], [0], id='Example: [[0], [0]]'),
        pytest.param([[1, 3, 2], [1, 2, 3]], [1, 3, 2], id='Example: [[1, 3, 2], [1, 2, 3]]'),
        pytest.param([[10], [50], [40], [50], [25, 25]], [50], id='Example: [[10], [50], [40], [50], [25, 25]]'),
    ],
)
def test_task_5_correct_work(test_input, expected):
    output = task_5(test_input)
    assert output == expected, (
        "See tests!"
    )


@pytest.mark.parametrize(
    'test_input, expected',
    [
        pytest.param(111, 111, id='Example: 111'),
        pytest.param(123, 321, id='Example: 123'),
        pytest.param(-123, -321, id='Example: -123'),
        pytest.param(2550, 552, id='Example: 2550'),
        pytest.param(0, 0, id='Example: 0'),
    ],
)
def test_task_6_correct_work(test_input, expected):
    output = task_6(test_input)
    assert output == expected, (
        "See tests!"
    )


@pytest.mark.parametrize(
    'test_input, expected',
    [
        pytest.param("aba", "b", id='Example: aba'),
        pytest.param("aaaccc", None, id='Example: aaaccc'),
        pytest.param("aaacccb", "b", id='Example: aaacccb'),
        pytest.param("", None, id='Example: '),
        pytest.param("empty", "e", id='Example: empty'),
        pytest.param("eempty", "m", id='Example: eempty'),
        pytest.param("emptye", "m", id='Example: emptye'),
        pytest.param("guccigu", "i", id='Example: guccigu'),
        pytest.param("guccigu", "i", id='Example: guccigu'),
        pytest.param("abcdfg", "a", id='Example: abcdfg'),
    ],
)
def test_task_7_correct_work(test_input, expected):
    output = task_7(test_input)
    assert output == expected, (
        "See tests!"
    )


@pytest.mark.parametrize(
    'test_input, expected',
    [
        pytest.param([0], [0], id='Example: [0]'),
        pytest.param([1, 2, 3], [6, 3, 2], id='Example: [1,2,3]'),
        pytest.param([1, 0, 0, 4], [0, 0, 0, 0], id='Example: [1, 0, 0, 4]'),
        pytest.param([3, 0], [0, 3], id='Example: [3, 0]'),
        pytest.param([3], [3], id='Example: [3]'),
        pytest.param([5, 5, 5, 5], [125, 125, 125, 125], id='Example: [5, 5, 5, 5]'),
    ],
)
def test_task_8_correct_work(test_input, expected):
    output = task_8(test_input)
    assert output == expected, (
        "See tests!"
    )