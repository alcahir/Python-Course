from typing import List


def task_1(array: List[int], target: int) -> List[int]:
    seen = {}
    for num in array:
        complement = target - num
        if complement in seen:
            return [complement, num]
        seen[num] = True
    return []


def task_2(number: int) -> int:
    result = 0
    number = abs(number)
    while number > 0:
        result = result * 10 + number % 10
        number //= 10
    return result


def task_3(array: List[int]) -> int:
    for i in range(len(array)):
        val = abs(array[i]) - 1
        if array[val] < 0:
            return abs(array[i])
        array[val] = -array[val]
    return -1


def task_4(string: str) -> int:
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(string)):
        if i + 1 < len(string) and roman[string[i]] < roman[string[i + 1]]:
            result -= roman[string[i]]
        else:
            result += roman[string[i]]
    return result


def task_5(array: List[int]) -> int:
    smallest = array[0]
    for num in array[1:]:
        if num < smallest:
            smallest = num
    return smallest
