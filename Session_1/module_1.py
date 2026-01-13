from typing import List
from itertools import combinations


def task_1(array: List[int], target: int) -> List[int]:
    pairs = list(combinations(array, 2))
    for i in pairs:
        if sum(i) == target:
            return list(i)
        else:
            continue
    return []


def task_2(number: int) -> int:
    res = 0
    if number > 0:
        while number > 0:
            res = res * 10 + number % 10
            number = number // 10
        return res
    elif number < 0:
        number = abs(number)
        while number > 0:
            res = res * 10 + number % 10
            number = number // 10
        return (-1) * res
    else:
        return 0


def task_3(array: List[int]) -> int:
    for i in range(len(array)):
        idx = abs(array[i]) - 1

        if array[idx] < 0:
            return abs(array[i])

        array[idx] *= -1

    return -1


def task_4(string: str) -> int:
    dictionary = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    n = len(string)
    for i in range(n - 1):
        if dictionary[string[i]] < dictionary[string[i + 1]]:
            total -= dictionary[string[i]]
        else:
            total += dictionary[string[i]]
    total += dictionary[string[-1]]
    return total


def task_5(array: List[int]) -> int:
    min = array[0]
    for i in array[1:]:
        if i < min:
            min = i
    return min
