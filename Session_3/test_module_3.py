import re

import numpy as np
import pytest
from module_3 import task_1, task_2, task_3, task_4, task_5, task_6


@pytest.mark.parametrize(
    "exp, bases, expected",
    [
        pytest.param(
            3, [0, 2, 3, 4], [0, 8, 27, 64], id="Example: exp 3, base [0, 1, 2, 3]"
        ),
        pytest.param(
            0, [0, 1, 5, 10], [1, 1, 1, 1], id="Example: exp 0, base [0, 1, 5, 10]"
        ),
        pytest.param(
            -1,
            [1, 5, 10, -1, -5, -10],
            [1.0, 0.2, 0.1, -1.0, -0.2, -0.1],
            id="Example: exp -1, base [1, 5, 10, -1, -5, -10]",
        ),
    ],
)
def test_task_1_correct_work(exp, bases, expected):
    power = task_1(exp)

    for idx in range(len(bases)):
        out = power(bases[idx])
        assert out == expected[idx], "Incorrect power operation result."


def test_task_2_correct_print(capsys):
    task_2(1, 2, 3, moment=4, cap="arkadiy")
    expected = "1\n2\n3\n4\narkadiy\n"
    out, err = capsys.readouterr()

    assert expected in out, f"Positional argument {1} is missed"


def test_task_3_correct_decorator_print(capsys):
    task_3("Egor")
    expected = (
        "Hi, friend! What's your name?\n" "Hello! My name is Egor.\n" "See you soon!\n"
    )

    out, err = capsys.readouterr()

    assert expected == out, "Incorrect decorators' prints"


def test_task_4_correct_time_management(capsys):
    task_4()
    out, err = capsys.readouterr()
    run_time = float(re.search(r"[+-]?([0-9]*[.])[0-9]+", "task_4 0.01").group(0))

    assert 0 < run_time < 5, "You have a weak PC :)"


@pytest.mark.parametrize(
    "size",
    [
        pytest.param((3, 3), id="Example: 3x3 matrix"),
        pytest.param((5, 5), id="Example: 5x5 matrix"),
        pytest.param((1, 1), id="Example: 1x1 matrix"),
        pytest.param((5, 3), id="Example: 5x3 matrix"),
        pytest.param((3, 5), id="Example: 3x5 matrix"),
    ],
)
def test_task_5_correct_work(size):
    matrix = np.random.rand(*size)
    transposed_matrix_np = matrix.T
    transposed_matrix_task = task_5(matrix)

    assert np.allclose(
        transposed_matrix_np, transposed_matrix_task
    ), f"Wrong transpose of matrix {matrix}"


@pytest.mark.parametrize(
    "brackets, expected",
    [
        pytest.param("((()))", True, id="Example: ((()))"),
        pytest.param("(", False, id="Example: ("),
        pytest.param(")()", False, id="Example: )()"),
        pytest.param("()()()()", True, id="Example: ()()()()"),
        pytest.param("(())()((()()))", True, id="Example: (())()((()()))"),
        pytest.param(")))", False, id="Example: )))"),
        pytest.param("())(()", False, id="Example: ())(()"),
    ],
)
def test_task_6_correct_work(brackets, expected):
    is_correct_brackets = task_6(brackets)
    assert is_correct_brackets == expected, "Incorrect answer. Check tests!"
