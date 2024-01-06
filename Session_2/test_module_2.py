import pytest
from module_2 import task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8


@pytest.mark.parametrize(
    "test_input_1, test_input_2, expected",
    [
        pytest.param(
            {"a": 123, "b": 23, "c": 0},
            {"a": 1, "b": 11, "d": 99},
            {"a": 124, "b": 34, "c": 0, "d": 99},
            id="Example: {'a': 123, 'b': 23, 'c' : 0}, {'a' : 1, 'b': 11, 'd': 99}",
        ),
        pytest.param(
            {"a": 123},
            {"b": 11},
            {"a": 123, "b": 11},
            id="Example: {'a': 123}, {'b': 11}",
        ),
        pytest.param({}, {}, {}, id="Example: {}, {}"),
        pytest.param({"a": 31}, {}, {"a": 31}, id="Example: {'a': 31}, {}"),
        pytest.param({}, {"a": 31}, {"a": 31}, id="Example: {}, {'a': 31}"),
    ],
)
def test_task_1_correct_work(test_input_1, test_input_2, expected):
    output = task_1(test_input_1, test_input_2)

    for key, value in expected.items():
        assert output.get(key) is not None, f"Your result doesn't have {key} key"
        assert (
            output.get(key) == value
        ), f"Key-{key} should has {value} value against {output.get(key)}"


def test_2_correct_work():
    output = task_2()
    expected = {idx: idx**2 for idx in range(1, 16)}

    for key, value in expected.items():
        assert output.get(key) is not None, f"Your result doesn't have {key} key"
        assert (
            output.get(key) == value
        ), f"Key-{key} should has {value} value against {output.get(key)}"


@pytest.mark.parametrize(
    "test_input, expected",
    [
        pytest.param(
            {"1": ["a", "b"], "2": ["c", "d"]},
            ["ac", "ad", "bc", "bd"],
            id="Example: {'1': ['a', 'b'], '2': ['c', 'd']}",
        ),
        pytest.param(
            {"1": ["a", "b"], "2": ["c", "d"], "3": ["d", "e"]},
            ["acd", "ace", "add", "ade", "bcd", "bce", "bdd", "bde"],
            id="Example: {'1':['a', 'b'], '2':['c', 'd'], '3': ['d', 'e']}",
        ),
        pytest.param(
            {"1": ["b"], "2": ["c", "b"]},
            ["bc", "bb"],
            id="Example: {'1': ['b'], '2': ['c', 'b']}",
        ),
    ],
)
def test_task_3_correct_work(test_input, expected):
    output = task_3(test_input)

    assert len(output) == len(expected), "Incorrect length"
    assert set(output) == set(expected), "Combination Mismatch"


@pytest.mark.parametrize(
    "test_input, expected",
    [
        pytest.param(
            {"a": 500, "b": 5874, "c": 560, "d": 400, "e": 5874, "f": 20},
            ["b", "e", "c"],
            id="Example: {'a': 500, 'b': 5874, 'c': 560,'d': 400, 'e': 5874, 'f': 20}",
        ),
        pytest.param(
            {"a": 500, "b": 5874, "c": 560},
            ["a", "b", "c"],
            id="Example: {'a': 500, 'b': 5874, 'c': 560}",
        ),
        pytest.param(
            {"a": -1, "b": 5874, "c": 560, "d": -30},
            ["a", "b", "c"],
            id="Example: {'a': -1, 'b': 5874, 'c': 560, 'd': -30}",
        ),
        pytest.param({"a": -1}, ["a"], id="Example: {'a': -1}"),
        pytest.param({}, [], id="Example: {}"),
    ],
)
def test_task_4_correct_work(test_input, expected):
    output = task_4(test_input)
    assert set(output) == set(expected), "See tests!"


@pytest.mark.parametrize(
    "test_input, expected",
    [
        pytest.param(
            [("yellow", 1), ("blue", 2), ("yellow", 3), ("blue", 4), ("red", 1)],
            {"yellow": [1, 3], "blue": [2, 4], "red": [1]},
            id="Example: [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]",
        ),
    ],
)
def test_task_5_correct_work(test_input, expected):
    output = task_5(test_input)

    for key, values in expected.items():
        assert output.get(key) is not None, f"Your result doesn't have {key} key"
        assert list(sorted(output.get(key))) == list(
            sorted(values)
        ), f"Key-{key} should has {values} value against {output.get(key)}"


@pytest.mark.parametrize(
    "test_input, expected",
    [
        pytest.param(
            ["1", "2", 1, 2],
            ["1", "2", 1, 2],
            id='Example: ["1", "2", 1, 2]',
        ),
        pytest.param(
            ["1", "2", 1, 1, 2, 2],
            ["1", "2", 1, 2],
            id='Example: ["1", "2", 1, 1, 2, 2],',
        ),
        pytest.param(
            [2, 2, 2],
            [2],
            id="Example: [2, 2, 2]",
        ),
        pytest.param(
            ["2", 2, 2, 2],
            ["2", 2],
            id='Example: ["2", 2, 2, 2]',
        ),
        pytest.param(
            ["2", 2.0, 2.1, 2],
            ["2", 2.0, 2.1],
            id='Example: ["2", 2.0, 2.1, 2]',
        ),
    ],
)
def test_task_6_correct_work(test_input, expected):
    output = task_6(test_input)

    assert set(output) == set(expected), "See tests!"


@pytest.mark.parametrize(
    "test_input, expected",
    [
        pytest.param(
            ["flower", "flows"],
            "flow",
            id='Example: ["flower", "flows"]',
        ),
        pytest.param(
            ["sun", "recap"],
            "",
            id='Example: ["sun", "recap"]',
        ),
        pytest.param(
            ["wonderful", "wonderful"],
            "wonderful",
            id='Example: ["wonderful", "wonderful"]',
        ),
        pytest.param(
            ["", ""],
            "",
            id='Example: ["", ""]',
        ),
        pytest.param(
            ["", "obama"],
            "",
            id='Example: ["", "obama"]',
        ),
        pytest.param(["oke", "eko"], "", id='Example: ["oke", "eko"]'),
        pytest.param(["abf", "abc", "acd"], "a", id='Example: ["abf", "abc", "acd"]'),
    ],
)
def test_task_7_correct_work(test_input, expected):
    output = task_7(test_input)

    assert output == expected, "See tests!"


@pytest.mark.parametrize(
    "test_input_1, test_input_2, expected",
    [
        pytest.param(
            "Star Killer",
            "Killer",
            5,
            id='Example: "Star Killer" find Killer',
        ),
        pytest.param(
            "Star Killer",
            "Miller",
            -1,
            id='Example: "Star Killer" find Miller',
        ),
        pytest.param(
            "Star Killer",
            "Star",
            0,
            id='Example: "Star Killer" find Star',
        ),
        pytest.param(
            "Star Killer",
            "l",
            7,
            id='Example: "Star Killer" find l',
        ),
        pytest.param(
            "Star Killer",
            "StarKiller",
            -1,
            id='Example: "Star Killer" find StarKiller',
        ),
        pytest.param(
            "Star Killer",
            "",
            0,
            id='Example: "Star Killer" find ""',
        ),
        pytest.param(
            "",
            "anything",
            -1,
            id="Example: in empty string find `anything`",
        ),
    ],
)
def test_task_8_correct_work(test_input_1, test_input_2, expected):
    output = task_8(test_input_1, test_input_2)

    assert output == expected, "See tests!"
