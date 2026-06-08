from typing import List


def task_1(array: List[int], target: int) -> List[int]:
    r = {}
    for i, n in enumerate(array):
        # enumerate -- return the value and index
        if target - n in r:
            return [n, target - n]
        else:
            r[n] = i


def task_2(number: int) -> int:
    if number < 0:   # for sign
        sign = -1
    else:
        sign = 1

    number = abs(number)
    result = 0

    while number > 0:
        digit = number % 10
        result = result * 10 + digit
        number = int(number / 10)
    return sign * result


def task_3(array: List[int]) -> int:
    d = {}

    for i in array:
        if i not in d:
            d[i] = 1
        else:
            return i

    return -1


def task_4(string: str) -> int:
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0

    for i in range(len(string)):
        current_value = roman[string[i]]

        if i + 1 < len(string) and current_value < roman[string[i + 1]]:
            total -= current_value
        else:
            total += current_value

    return total


def task_5(array: List[int]) -> int:
    m = array[0]
    for i in range(1, len(array)-1):
        if m > array[i]:
            m = array[i]
    return m
