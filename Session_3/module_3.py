import time
from typing import List


Matrix = List[List[int]]


def task_1(exp: int):
    def power(number):
        return number ** exp
    return power


def task_2(*args, **kwargs):
    for arg in args:
        print(arg)

    for value in kwargs.values():
        print(value)


def helper(func):
    def wrapper(*args, **kwargs):
        print("Hi, friend! What's your name?")
        func(*args, **kwargs)
        print("See you soon!")
    return wrapper


@helper
def task_3(name: str):
    print(f"Hello! My name is {name}.")


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        run_time = time.time() - start_time
        print(f"Finished {func.__name__} in {run_time:.4f} secs")

        return result
    return wrapper


@timer
def task_4():
    return len([1 for _ in range(0, 10 ** 8)])


def task_5(matrix: Matrix) -> Matrix:
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    result = []

    for col in range(cols):
        new_row = []

        for row in range(rows):
            new_row.append(matrix[row][col])

        result.append(new_row)

    return result


def task_6(queue: str):
    balance = 0

    for char in queue:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1

        if balance < 0:
            return False

    return balance == 0
