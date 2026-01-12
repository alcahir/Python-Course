from typing import List


def task_1(array: List[int], target: int) -> List[int]:
    seen = {}  # value -> index

    for i, num in enumerate(array):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []
    pass


def task_2(number: int) -> int:
    """
    Write your code below
    """
    pass


def task_3(array: List[int]) -> int:
    """
    Write your code below
    """
    pass


def task_4(string: str) -> int:
    """
    Write your code below
    """
    pass


def task_5(array: List[int]) -> int:
    """
    Write your code below
    """
    pass
