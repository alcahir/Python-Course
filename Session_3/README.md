
## Tasks

#### Task 1
Write a Python function `task_1` to do power factory. You need to implement enclosing scope as closure.  
Your closure factory function power_factory() takes an argument called `exp`.  
You can use this function to build closures that run different power operations.
```python 
>>> power = task_1(3)
>>> power(3)
27
>>> power(4)
64
>>> power(0)
0
```

#### Task 2
Write a Python function `task_2` that can accept any num of positional and keyword arguments.
You need to print each value of argument in the order it's passed to the function.
```python 
>>> task_2(1, 2, 3, moment=4, cap="arkadiy")
1
2
3
4
arkadiy
```

#### Task 3
Write a Python decorator `helper` to simulate the following behavior. 
```python
@helper 
task_3
>>> task_3("John")
Hi, friend! What's your name?
Hello! My name is John.
See you soon!
```

#### Task 4
Write a Python decorator `timer` to measure runtime of function `task_4`.  
Note: Use `print(f"Finished {func.__name__} in {run_time:.4f} secs")` for printing result.
```python
@timer
task_4

>>> task_4()
Finished task_4 in 4.4489 secs
```

#### Task 5
Write a Python function `task_5` to transpose 2D matrix.  
Given a 2D integer array matrix, return the transpose of matrix.  
The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.


### Optional

#### Task 6
Write a Python function `task_6` to find validity of a string of parentheses, '(', ')'.  
These brackets must be close in the correct order, for example "()".  
```python
>>> task_6("((()))")
True

>>> task_6(")()")
False
```
