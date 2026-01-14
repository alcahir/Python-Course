# import time
from typing import List

Matrix = List[List[int]]


def task_1(exp: int):
    def power_factory(exp_inner: int):
        def power(x: int) -> int:
            return x ** exp_inner
        return power

    return power_factory(exp)


def task_2(*args, **kwags):
    for v in args:
        print(v)
    for v in kwags.values():
        print(v)


def helper(func):
    def wrapper(*args, **kwargs):
        print("Hi, friend! What's your name?")
        result = func(*args, **kwargs)
        print("See you soon!")
        return result
    return wrapper


@helper
def task_3(name: str):
    print(f"Hello! My name is {name}.")


def timer(func):
    cimport time

    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        run_time = time.perf_counter() - start
        print(f"Finished {func.__name__} in {run_time:.4f} secs")
        return result

    return wrapper


@timer
def task_4():
    return len([1 for _ in range(0, 10**8)])


def task_5(matrix: Matrix) -> Matrix:
    if not matrix:
        return []
    # assumes rectangular matrix
    return [list(row) for row in zip(*matrix)]


def task_6(queue: str):
    balance = 0
    for ch in queue:
        if ch == "(":
            balance += 1
        elif ch == ")":
            balance -= 1
            if balance < 0:
                return False
        else:
            # if any other chars appear, treat as invalid
            return False
    return balance == 0
