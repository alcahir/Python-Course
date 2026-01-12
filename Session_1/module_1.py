from typing import List


def task_1(array: List[int], target: int) -> List[int]:
    checked_nums = set()
    for num in array:
        s_num = target - num
        if s_num in checked_nums:
            return [num, s_num]
        checked_nums.add(num)
    return []


def task_2(number: int) -> int:
    res_num = 0
    sign = -1 if number < 0 else 1
    number = abs(number)
    while number > 0:
        res_num = res_num * 10 + number % 10
        number //= 10

    return sign * res_num


def task_3(array: List[int]) -> int:
    myDict = dict()
    for i in array:
        if i in myDict:
            if myDict[i] + 1 == 2:
                return i
        else:
            myDict[i] = 1
    return -1


def task_4(string: str) -> int:
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0
    string = string.replace("IV", "IIII").replace("IX", "VIIII")
    string = string.replace("XL", "XXXX").replace("XC", "LXXXX")
    string = string.replace("CD", "CCCC").replace("CM", "DCCCC")
    for char in string:
        number += translations[char]
    return number


def task_5(array: List[int]) -> int:
    min_num = array[0]
    for ii in range(1, len(array)):
        if min_num > array[ii]:
            min_num = array[ii]
    return min_num
