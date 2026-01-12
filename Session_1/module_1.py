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
        digit = number % 10
        result = result * 10 + digit
        number //= 10
    return result


def task_3(array: List[int]) -> int:
    for i in range(len(array)):
        value = abs(array[i])
        index = value - 1

        if array[index] < 0:
            return value

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
    for num in array[1:]:
        if num < smallest:
            smallest = num
    return smallest
