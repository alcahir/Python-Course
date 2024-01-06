import pytest
from module_1 import task_1, task_2, task_3, task_4, task_5


@pytest.mark.parametrize(
    "test_input, expected",
    [
        pytest.param(
            ([2, 7, 11, 15], 9), [2, 7], id="Example: sample=[2, 7, 11, 15], target=9"
        ),
        pytest.param(([3, 2, 4], 6), [2, 4], id="Example: sample=[3, 2, 4], target=6"),
        pytest.param(([3, 3], 6), [3, 3], id="Example: sample=[3, 3], target=6"),
        pytest.param(
            ([2, 5, 5, 11], 10), [5, 5], id="Example: sample=[2, 5, 5, 11], target=10"
        ),
        pytest.param(([2], 2), [], id="Example: sample=[2], target=2"),
        pytest.param(([2, 3], 5), [2, 3], id="Example: sample=[2, 3], target=5"),
        pytest.param(
            ([-1, 2, 12, 5, 111, -3], 9),
            [12, -3],
            id="Example: sample=[-1, 2, 12, 5, 111, -3], target=9",
        ),
        pytest.param(
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], 17),
            [8, 9],
            id="Example: sample=[1, 2, 3, 4, 5, 6, 7, 8, 9], target=17",
        ),
        pytest.param(([], 18), [], id="Example: sample=[], target=18"),
        pytest.param(([-1, -1], 2), [], id="Example: sample=[-1, -1], target=2"),
    ],
)
def test_task_1(test_input, expected):
    assert sorted(task_1(*test_input)) == sorted(expected)


@pytest.mark.parametrize(
    "test_input, expected",
    [
        pytest.param(12, 21, id="Example: sample=123"),
        pytest.param(-123, -321, id="Example: sample=-123"),
        pytest.param(120, 21, id="Example: sample=120"),
        pytest.param(0, 0, id="Example: sample=0"),
        pytest.param(555, 555, id="Example: sample=555"),
        pytest.param(10, 1, id="Example: sample=1"),
        pytest.param(-10, -1, id="Example: sample=-1"),
        pytest.param(100, 1, id="Example: sample=100"),
    ],
)
def test_task_2(test_input, expected):
    assert task_2(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        pytest.param(
            [2, 1, 5, 2, 3, 3, 4], 2, id="Example: sample=[2, 1, 5, 2, 3, 3, 4]"
        ),
        pytest.param(
            [2, 1, 5, 3, 3, 2, 4], 3, id="Example: sample=[2, 1, 5, 3, 3, 2, 4]"
        ),
        pytest.param(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            -1,
            id="Example: sample=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]",
        ),
        pytest.param(
            [1, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            1,
            id="Example: sample=[1, 1, 2, 3, 4, 5, 6, 7, 8, 9]",
        ),
        pytest.param(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],
            1,
            id="Example: sample=[1, 2, 3, 4, 5, 6, 7, 8, 9, 1]",
        ),
        pytest.param(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 9],
            9,
            id="Example: sample=[1, 2, 3, 4, 5, 6, 7, 8, 9, 9]",
        ),
        pytest.param(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5],
            5,
            id="Example: sample=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5]",
        ),
        pytest.param(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            -1,
            id="Example: sample=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1]",
        ),
        pytest.param([], -1, id="Example: sample=[]"),
    ],
)
def test_task_3(test_input, expected):
    assert task_3(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        pytest.param("III", 3, id="Example: sample=III"),
        pytest.param("IV", 4, id="Example: sample=IV"),
        pytest.param("IX", 9, id="Example: sample=IX"),
        pytest.param("LVIII", 58, id="Example: sample=LVIII"),
        pytest.param("MCMXCIV", 1994, id="Example: sample=MCMXCIV"),
        pytest.param("MMXXI", 2021, id="Example: sample=MMXXI"),
        pytest.param("MMXX", 2020, id="Example: sample=MMXX"),
        pytest.param("MMXIX", 2019, id="Example: sample=MMXIX"),
        pytest.param("MMXVIII", 2018, id="Example: sample=MMXVIII"),
        pytest.param("MMXVII", 2017, id="Example: sample=MMXVII"),
        pytest.param("MMXVI", 2016, id="Example: sample=MMXVI"),
        pytest.param("MMXV", 2015, id="Example: sample=MMXV"),
        pytest.param("MMXIV", 2014, id="Example: sample=MMXIV"),
        pytest.param("MCMXCIV", 1994, id="Example: sample=MCMXCIV"),
        pytest.param("MCMXCIII", 1993, id="Example: sample=MCMXCIII"),
        pytest.param("MCMXCII", 1992, id="Example: sample=MCMXCII"),
        pytest.param("C", 100, id="Example: sample=C"),
        pytest.param("D", 500, id="Example: sample=D"),
        pytest.param("M", 1000, id="Example: sample=M"),
        pytest.param("L", 50, id="Example: sample=L"),
        pytest.param("V", 5, id="Example: sample=V"),
        pytest.param("I", 1, id="Example: sample=I"),
        pytest.param("II", 2, id="Example: sample=II"),
        pytest.param("VI", 6, id="Example: sample=VI"),
        pytest.param("VII", 7, id="Example: sample=VII"),
        pytest.param("VIII", 8, id="Example: sample=VIII"),
        pytest.param("XI", 11, id="Example: sample=XI"),
    ],
)
def test_task_4(test_input, expected):
    assert task_4(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        pytest.param([3, 4, 5, 1, 2], 1, id="Example: sample=[3, 4, 5, 1, 2]"),
        pytest.param(
            [4, 5, 6, 7, 0, 1, 2], 0, id="Example: sample=[4, 5, 6, 7, 0, 1, 2]"
        ),
        pytest.param([11, 13, 15, 17], 11, id="Example: sample=[11, 13, 15, 17]"),
        pytest.param(
            [1, 2, 3, 4, 5, 6, 7], 1, id="Example: sample=[1, 2, 3, 4, 5, 6, 7]"
        ),
        pytest.param(
            [1, 2, 3, 4, 5, 6, 7, 0], 0, id="Example: sample=[1, 2, 3, 4, 5, 6, 7, 0]"
        ),
        pytest.param(
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            1,
            id="Example: sample=[1, 2, 3, 4, 5, 6, 7, 8, 9]",
        ),
        pytest.param([-1, 1, 0], -1, id="Example: sample=[-1, 1, 0]"),
        pytest.param([1, 0], 0, id="Example: sample=[1, 0]"),
        pytest.param([1], 1, id="Example: sample=[1]"),
        pytest.param([-3, 5, 10, -2, -5, 50, 0], -5, id="Example: sample=[1, 2]"),
    ],
)
def test_task_5(test_input, expected):
    assert task_5(test_input) == expected
