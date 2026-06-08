from typing import List


def task_1(array: List[int], target: int) -> List[int]:
    """
    Write your code below
    """
    # sample = [3, 4, -1, 10, 12] target = 2

    checked_numbers = set()

    for number in array:

        difference = target - number

        if difference in checked_numbers:
            return [difference, number]

        checked_numbers.add(number)

    return []


def task_2(number: int) -> int:
    """
    Write your code below
    """
    # sample = 130 output = 31

    is_negative = number < 0
    num = abs(number)
    reversed_number = 0

    while num > 0:
        last_digit = num % 10

        reversed_number = (reversed_number * 10) + last_digit

        num = num // 10

    if is_negative:
        reversed_number = -reversed_number

    return reversed_number


def task_3(array: List[int]) -> int:
    """
    Write your code below
    """
    # sample = [2, 1, 3, 4, 2] output = 2

    for number in array:
        num = abs(number)

        index = num - 1

        if array[index] < 0:
            return num

        array[index] = -array[index]

    return -1


def task_4(string: str) -> int:
    """
    Write your code below
    """

    roman_numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    total = 0
    length = len(string)

    for i in range(length):
        current_num = roman_numbers[string[i]]

        if i + 1 < length:
            next_num = roman_numbers[string[i + 1]]

            if current_num < next_num:
                total -= current_num
            else:
                total += current_num

        else:
            total += current_num

    return total


def task_5(array: List[int]) -> int:
    """
    Write your code below
    """

    smallest_number = array[0]

    for number in array:
        if number < smallest_number:
            smallest_number = number

    return smallest_number
