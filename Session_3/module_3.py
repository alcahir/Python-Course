# import time
from typing import List

Matrix = List[List[int]]


def task_1(exp: int):
    def power(x):
        powered = x**exp
        print(powered)
        return powered
    return power

def task_2(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(value)

def helper(func):
    def wrapper(name):
        print("Hi, friend! What's your name?")
        func(name)
        print("See you soon!")
    return wrapper

@helper
def task_3(name: str):
    print(f"Hello! My name is {name}.")

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__} in {run_time:.4f} secs")
        return result

    return wrapper

@timer
def task_4():
    return len([1 for _ in range(0, 10 ** 8)])



def task_5(matrix: Matrix) -> Matrix:
    num_rows = len(matrix)
    num_columns = len(matrix[0])

    Matrix = []
    for j in range(num_columns):
        new_row = []
        for i in range(num_rows):
            new_row.append(matrix[i][j])
        Matrix.append(new_row)

    return Matrix
