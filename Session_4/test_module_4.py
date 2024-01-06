import pytest
from module_4 import Trainee


@pytest.fixture()
def trainee_chetan():
    return Trainee("Chetan", "Jakkoju")


def test_visit_lecture_correct_work(trainee_chetan):
    for i in range(11):
        trainee_chetan.visit_lecture()

    assert 11 == trainee_chetan.visited_lectures, "Incorrect number of visited lectures"
    assert 10 == trainee_chetan.mark, "Incorrect mark"


def test_do_homework_correct_work(trainee_chetan):
    for i in range(5):
        trainee_chetan.do_homework()

    assert 10 == trainee_chetan.done_home_tasks, "Incorrect number of done home tasks"
    assert 10 == trainee_chetan.mark, "Incorrect mark"


def test_miss_lecture_correct_work(trainee_chetan):
    for i in range(3):
        trainee_chetan.miss_lecture()

    assert -3 == trainee_chetan.missed_lectures, "Incorrect number of missed lectures"
    assert 0 == trainee_chetan.mark, "Incorrect mark"


def test_miss_homework_correct_work(trainee_chetan):
    for i in range(3):
        trainee_chetan.miss_homework()

    assert -6 == trainee_chetan.missed_home_tasks, "Incorrect number of missed lectures"
    assert 0 == trainee_chetan.mark, "Incorrect mark"


def test_pass_trainee_correct_result(trainee_chetan, capsys):
    for i in range(5):
        trainee_chetan.do_homework()

    for i in range(2):
        trainee_chetan.miss_lecture()

    trainee_chetan.is_passed()

    out, err = capsys.readouterr()

    assert 8 == trainee_chetan.mark, "Incorrect mark"

    assert "Good job!" in out, "You don't print 'Good job!'"


def test_fail_trainee_correct_work(trainee_chetan, capsys):
    for i in range(5):
        trainee_chetan.do_homework()
        trainee_chetan.miss_lecture()

    trainee_chetan.is_passed()

    out, err = capsys.readouterr()

    assert 5 == trainee_chetan.mark, "Incorrect mark"

    assert (
        "You need to 3 points. Try to do your best!" in out
    ), "Incorrect print when you fail exam. Check the current mark."


def test_mark_under_ten_after_many_actions(trainee_chetan, capsys):
    for i in range(3):
        trainee_chetan.visit_lecture()
        trainee_chetan.do_homework()
    trainee_chetan.do_homework()

    trainee_chetan.is_passed()

    out, err = capsys.readouterr()

    assert 10 == trainee_chetan.mark, "Incorrect mark"

    assert "Good job!" in out, "You don't print 'Good job!'"


def test_mark_non_negative_after_many_actions(trainee_chetan, capsys):
    trainee_chetan.visit_lecture()
    trainee_chetan.do_homework()
    trainee_chetan.miss_lecture()

    for i in range(3):
        trainee_chetan.visit_lecture()
        trainee_chetan.miss_homework()

    trainee_chetan.is_passed()

    out, err = capsys.readouterr()

    assert 0 == trainee_chetan.mark, "Incorrect mark"

    assert (
        "You need to 8 points. Try to do your best!" in out
    ), "Incorrect print when you fail exam. Check the current mark."
