﻿
## Tasks

#### Task 1
<<<<<<< HEAD
Write a Python function `task_1` to find those numbers which are divisible by 3 and multiple of 5, between 1 and  1000 (both included).  
Return list of correct numbers.

#### Task 2
Write a Python function `task_2` that accepts a string and calculate the number(integers) of digits and letters(english).  
=======
Write a Python function `task_1` to find those numbers which are divisible by 3 and multiple of 5, between 1 and  1000 (both included).__
Return list of correct numbers.

#### Task 2
Write a Python function `task_2` that accepts a string and calculate the number(integers) of digits and letters(english).__
>>>>>>> 2a7fb222acad7d976174429b5bcf8a39a703d279
Return num of digits and num of letters.
Example:
```python
>>> task_2("12abd3")
(3,3)
>>> task_2("13454")
(5, 0)
>>> task_2("bad")
(0, 3)
```

#### Task 3
<<<<<<< HEAD
Write a Python function `task_3` to compute the difference between two lists. __Each list consists of unique values!__  
Return tuple of differences.  
Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]  
Color1-Color2: ['white', 'orange', 'red']  
Color2-Color1: ['black', 'yellow']  
=======
Write a Python function `task_3` to compute the difference between two lists. __Each list consists of unique values!__ <br />
Return tuple of differences.__
Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]__
Color1-Color2: ['white', 'orange', 'red']__
Color2-Color1: ['black', 'yellow']__
>>>>>>> 2a7fb222acad7d976174429b5bcf8a39a703d279
```python
>>> task_3(["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"])
(['white', 'orange', 'red'], ['black', 'yellow'])
```

#### Task 4
Write a Python function `task_4` to convert a list of multiple integers(non-negative) into a single integer. 
Example:
```python
>>> task_4([11, 44, 33])
114433
```

#### Task 5
<<<<<<< HEAD
Write a Python function `task_5` to find the list in a list of lists whose sum of elements is the highest.  
If the nested lists have the same max sum, then you need to return first of them.  
Return this list.  
=======
Write a Python function `task_5` to find the list in a list of lists whose sum of elements is the highest.__
If the nested lists have the same max sum, then you need to return first of them.__
Return this list.__
>>>>>>> 2a7fb222acad7d976174429b5bcf8a39a703d279
Example:
```python
>>> task_5([[1,2], [3], [0, 12, 17, 6]])
[0, 12, 17, 6]
```

### Optional

#### Task 6
Write a Python function `task_6` to reverse integer without usage of converting to str.
```python
>>> task_6(123)
321
>>> task_6(-132)
-231
>>> task_6(2550)
552
```

#### Task 7
<<<<<<< HEAD
Write a Python function `task_7` to find the first non-repeating character in given string.  
=======
Write a Python function `task_7` to find the first non-repeating character in given string.__
>>>>>>> 2a7fb222acad7d976174429b5bcf8a39a703d279
Return this symbol if it's existed. Otherwise, None has to be returned.
```python
>>> task_7("aba")
b
>>> task_7("aaaccc")
None
>>> task_7("aaacccb")
b
```

#### Task 8
<<<<<<< HEAD
Implement a Python function `task_8` with given list of integers.  
=======
Implement a Python function `task_8` with given list of integers.__
>>>>>>> 2a7fb222acad7d976174429b5bcf8a39a703d279
Return a new list such that each element at index `i` of the new list is the product of all the numbers in the original array except the one at `i`.
```python
>>> foo([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]

>>> foo([3, 2, 1])
[2, 3, 6]
```

## Materials

#### Python Materials
* __Learning Python__, 4th Edition By Mark Lutz
  * _Chapter 4_ Introducing Python Object Types
  * _Chapter 5_ Numeric Types
  * _Chapter 6_ The Dynamic Typing Interlude
  * _Chapter 7_ String Fundamentals
  * _Chapter 8_ Lists and Dictionaries
  * _Chapter 9_ Tuples, Files, and Everything Else
* [Data structures](https://docs.python.org/3.6/tutorial/datastructures.html)
* [Variables and Types](https://www.learnpython.org/en/Variables_and_Types)
* [Lists](https://www.learnpython.org/en/Lists)
* __Basic__ Python tutorial from [here](https://www.tutorialspoint.com/python/index.htm)
