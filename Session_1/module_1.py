from typing import List


def task_1(array: List[int], target: int) -> List[int]:
    seen = set()
    for x in array:
        needed = target - x
        if needed in seen:
            return [needed, x]
        seen.add(x)
    return []


def task_2(number: int) -> int:
    result = 0
    while number > 0:
        result = result * 10 + number % 10
        number //= 10
    return result


def task_3(array: List[int]) -> int:
    for i in range(len(array)):
        index = abs(array[i]) - 1
        if array[index] < 0:
            return abs(array[i])
        array[index] = -array[index]
    return -1


def task_4(string: str) -> int:
    values = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }
    total = 0
    for i in range(len(string)):
        if i + 1 < len(string) and values[string[i]] < values[string[i + 1]]:
            total -= values[string[i]]
        else:
            total += values[string[i]]
    return total


def task_5(array: List[int]) -> int:
    smallest = array[0]
    for x in array[1:]:
        if x < smallest:
            smallest = x
    return smallest
