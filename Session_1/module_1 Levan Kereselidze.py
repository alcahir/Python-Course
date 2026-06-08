from typing import List


def task_1(array: list[int], target: int) -> list[int]:
    for i in range(len(array)):
        if target - array[i] in array:
            return [array[i], target-array[i]]
    return []
    pass


def task_2(number: int) -> int:
    result = 0

    while number > 0:
        result = result * 10 + number % 10
        number //= 10

    return result


def task_3(array: List[int]) -> int:
    n = len(array)

    for i in range(n):
        for j in range(i + 1, n):
            if array[i] == array[j]:
                return array[i]

    return -1


def task_4(string: str) -> int:
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0

    for i in range(len(string)):
        current = values[string[i]]

        if i + 1 < len(string) and current < values[string[i + 1]]:
            result -= current
        else:
            result += current

    return result


def task_5(array: List[int]) -> int:
    minimum = array[0]

    for value in array:
        if value < minimum:
            minimum = value

    return minimum
