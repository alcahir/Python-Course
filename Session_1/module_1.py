from typing import List


def task_1(array: List[int], target: int) -> List[int]:
    if not array:
        return []
    seen = set()
    for num in array:
        complement = target - num
        if complement in seen:
            return [complement, num]
        seen.add(num)
    return []


def task_2(num: int) -> int:
    negative = num < 0
    num = abs(num)
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    return -reversed_num if negative else reversed_num


def task_3(array: List[int]) -> int:
    for i in range(len(array)):
        index = abs(array[i]) - 1
        if array[index] < 0:
            return abs(array[i])
        array[index] = -array[index]
    return -1


def task_4(s: str) -> int:
    d = {"I": 1, "V": 5, "L": 50, "X": 10, "C": 100, "D": 500, "M": 1000}
    res = 0
    for i in range(len(s)):
        a = d.get(s[i])
        res += a
        if i != len(s) - 1:
            if d.get(s[i]) < d.get(s[i + 1]):
                res -= 2 * d.get(s[i])
    return res


def task_5(array: List[int]) -> int:
    smallest = array[0]
    for num in array:
        if num < smallest:
            smallest = num
    return smallest

