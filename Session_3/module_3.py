# import time
from typing import List

Matrix = List[List[int]]


def task_1(exp: int):
    def power(n: int) -> int:
        return n ** exp
    return power



def task_2(*args, **kwargs):
    for value in args:
        print(value)
    for value in kwargs.values():
        print(value)



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

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        run_time = end - start
        print(f"Finished {func.__name__} in {run_time:.4f} secs")
        return result
    return wrapper

@timer
def task_4():
    return len([1 for _ in range(0, 10**8)])



def task_5(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    result = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        result.append(new_row)
    
    return result



def task_6(queue: str):
    pass
