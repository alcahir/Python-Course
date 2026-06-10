import time
from typing import List

Matrix = List[List[int]]


def task_1(exp: int):
    def power(x):
        return x ** exp
    return power


def task_2(*args, **kwargs):
    for value in args:
        print(value)

    for value in kwargs.values():
        print(value)


def helper(func):
    def wrapper(*args, **kwargs):
        print("Hi, friend! What's your name?")
        func(*args, **kwargs)
        print("See you soon!")
    return wrapper


@helper
def task_3(name):
    print(f"Hello! My name is {name}.")


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        run_time = end_time - start_time

        print(f"Finished {func.__name__} in {run_time:.4f} secs")
        return result

    return wrapper


def task_5(matrix: Matrix):
    result = []

    for col in range(len(matrix[0])):
        row = []

        for r in range(len(matrix)):
            row.append(matrix[r][col])

        result.append(row)

    return result


def task_6(queue: str):
    pass
