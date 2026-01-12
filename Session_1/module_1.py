from typing import List


def task_1(array: List[int], target: int) -> List[int]:
    seen = set()
    for num in array:
        complement = target - num
        if complement in seen:
            return [complement, num]
        seen.add(num)
    return []


def task_2(number: int) -> int:
    reversed_num = 0
    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number //= 10
    return reversed_num


def task_3(array: List[int]) -> int:
    for i in range(len(array)):
        val = abs(array[i])
        if array[val - 1] < 0:
            return val
        array[val - 1] *= -1
    return -1


def task_4(string: str) -> int:
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for char in reversed(string):
        curr = roman_map[char]
        if curr < prev:
            total -= curr
        else:
            total += curr
        prev = curr
    return total


def task_5(array: List[int]) -> int:
    if not array:
        raise ValueError("Empty array has no minimum value")
    smallest = array[0]
    for num in array:
        if num < smallest:
            smallest = num
    return smallest
