from typing import List
import time


def task_1(exp):
    def power(base):
        return base ** exp
    return power


def task_2(*args, **kwargs):
    for item in args:
        print(item)
    for entry in kwargs.values():
        print(entry)


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
        begin = time.time()
        output = func(*args, **kwargs)
        finish = time.time()
        run_time = finish - begin
        print(f"Finished {func.__name__} in {run_time:.4f} secs")
        return output
    return wrapper


@timer
def task_4():
    time.sleep(4.4489)


def task_5(matrix: List[List[int]]) -> List[List[int]]:
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    flipped = []
    for c in range(num_cols):
        line = []
        for r in range(num_rows):
            line.append(matrix[r][c])
        flipped.append(line)
    return flipped


def task_6(s: str) -> bool:
    counter = 0
    for ch in s:
        if ch == '(':
            counter += 1
        elif ch == ')':
            counter -= 1
        if counter < 0:
            return False
    return counter == 0
