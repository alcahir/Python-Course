import os
import sys
from io import BytesIO, TextIOWrapper
from unittest.mock import patch

import pytest
from module_5 import PATH_TO_OUTPUT, S5_PATH, task_1, task_2, task_3, task_4, task_5
from requests.exceptions import RequestException

EXPECTED_FILE = S5_PATH / "full_names.txt"
EPAM_URL = "https://www.epam.com/"
UNAVAILABLE_URL = "https://onlinelibrary.wiley.com/loi/14685922/"
BAD_AUTHORIZATION_URL = (
    "https://www.sciencedirect.com/journal/food-and-chemical-toxicology"
)


def test_task_sorted_full_names_exist():
    task_1()

    assert os.path.exists(
        PATH_TO_OUTPUT
    ), "sorted_names_and_surnames.txt does not exist in the directory where script module_5.py is!"


def test_task_1_correct_full_names():
    with (
        open(PATH_TO_OUTPUT, encoding="utf-8") as output,
        open(EXPECTED_FILE, encoding="utf-8") as expected,
    ):
        output = output.readlines()
        expected = expected.readlines()

    assert len(output) == len(
        expected
    ), f"The file should contain {len(expected)} rows against {len(output)}"

    for idx in range(len(expected)):
        expected_full_name = expected[idx].strip()
        output_full_name = output[idx].strip()

        assert (
            expected_full_name == output_full_name
        ), f"Incorrect full name {output_full_name}. Correct - {expected_full_name}"


@pytest.mark.parametrize(
    "top_k, expected",
    [
        pytest.param(
            3, [("blind", 101), ("far", 68), ("text", 67)], id="Example: top 3 words"
        ),
        pytest.param(
            5,
            [("blind", 101), ("far", 68), ("text", 67), ("copy", 66), ("way", 51)],
            id="Example: top 5 words",
        ),
    ],
)
def test_task_2_correct_work(top_k, expected):
    output = task_2(top_k)

    assert len(output) == len(expected), "Incorrect num of top words."

    for idx in range(len(expected)):
        assert (
            output[idx][0] == expected[idx][0]
        ), f"The words {output[idx][0]} should be {expected[idx][0]}"
        assert output[idx][1] == expected[idx][1], (
            f"True frequency of {expected[idx][0]} is {expected[idx][1]}. "
            f"Your frequency is {output[idx][1]}"
        )


@pytest.mark.parametrize(
    "url", [pytest.param(UNAVAILABLE_URL), pytest.param(BAD_AUTHORIZATION_URL)]
)
def test_task_3_correct_raise(url):
    with pytest.raises(RequestException) as excn:
        task_3(url)
    assert excn.type is RequestException


def test_task_3_correct_response():
    response = task_3(EPAM_URL)
    assert response.status_code == 200, "Incorrect status code"


@pytest.mark.parametrize(
    "test_input, expected",
    [
        pytest.param([1, 2, 3], 6, id="Example: [1, 2, 3]"),
        pytest.param(["0", 3, "2.1"], 5.1, id="Example: ['0', 3, '2.1']"),
        pytest.param(["1", "2", "3"], 6, id='Example: ["1", "2", "3"]'),
    ],
)
def test_task_4_correct_work(test_input, expected):
    output = task_4(test_input)

    assert output == expected, "Incorrect sum"


@pytest.mark.parametrize(
    "test_input, expected",
    [
        pytest.param("5 0".encode("utf-8"), "Can't divide by zero", id="Example: 5 0"),
        pytest.param("0 5.1".encode("utf-8"), "0", id="Example: 0 5.1"),
        pytest.param(
            "12 aba".encode("utf-8"), "Entered value is wrong", id="Example: 12 aba"
        ),
        pytest.param("12 6".encode("utf-8"), "2", id="Example: 12 6"),
        pytest.param("10 3".encode("utf-8"), "3.333", id="Example: 10 3"),
    ],
)
def test_task_5_division_by_zero(test_input, expected, capsys):
    with patch.object(
        sys,
        "stdin",
        TextIOWrapper(
            BytesIO(test_input),
            encoding="utf-8",
        ),
    ):
        task_5()
        out, err = capsys.readouterr()
        assert expected in out, "Incorrect result"
