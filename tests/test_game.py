from game import check_answer
from missions import MISSIONS


def test_correct_answer():
    assert check_answer(MISSIONS[0], "8")


def test_incorrect_answer():
    assert not check_answer(MISSIONS[0], "5")


def test_answer_with_spaces():
    assert check_answer(MISSIONS[0], " 8 ")