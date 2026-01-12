from typing import List


def task_1(array: List[int], target: int) -> List[int]:
    seen = set()
    for num in array:
        need = target - num
        if need in seen:
            return [need, num]
        seen.add(num)
    return []


def task_2(number: int) -> int:
    result = 0
    while number > 0:
        result = result * 10 + number % 10
        number //= 10
    return result


def task_3(array: List[int]) -> int:
    n = len(array)
    for i in range(n):
        index = abs(array[i]) - 1
        if array[index] < 0:
            return abs(array[i])
        array[index] = -array[index]
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

    total = 0
    prev = 0

    for char in reversed(string):
        curr = values[char]
        if curr < prev:
            total -= curr
        else:
            total += curr
        prev = curr

    return total


def task_5(array: List[int]) -> int:
    smallest = array[0]
    for num in array[1:]:
        if num < smallest:
            smallest = num
    return smallest
