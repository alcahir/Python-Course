
## Tasks

#### Task 2.1
Implement a function that receives as a named argument (incoming_data=[])
a list with dictionaries like below and makes sort of the elements
(dictionaries) by class (A, B, C, D, E, F) and returns it.
```python
[{'name': 'Vasia', 'age': 13, 'class': 'B'}, ...]
```
NOTE: For sorting purposes use dictionaries.

Style: `foo(incoming_data: List[dict]) -> List[dict]`

Implementation example:
```python

guys = [{'name': 'Petia', 'age': 8, 'class': 'A'},
        {'name': 'Slava', 'age': 17, 'class': 'F'},
        {'name': 'Ura', 'age': 15, 'class': 'E'},
        {'name': 'Sveta', 'age': 16, 'class': 'B'},
        {'name': 'Katia', 'age': 7, 'class': 'C'},
        {'name': 'Vova', 'age': 12, 'class': 'C'},
        {'name': 'Vika', 'age': 11, 'class': 'A'},
        {'name': 'Stas', 'age': 8, 'class': 'B'},
        {'name': 'Masha', 'age': 9, 'class': 'F'},]


print(foo(incoming_data=guys))
>>> [{'name': 'Petia', 'age': 8, 'class': 'A'},
     {'name': 'Vika', 'age': 11, 'class': 'A'},
     {'name': 'Sveta', 'age': 16, 'class': 'B'},
     {'name': 'Stas', 'age': 8, 'class': 'B'},
     {'name': 'Katia', 'age': 7, 'class': 'C'},
     {'name': 'Vova', 'age': 12, 'class': 'C'},
     {'name': 'Ura', 'age': 15, 'class': 'E'},
     {'name': 'Slava', 'age': 17, 'class': 'F'},
     {'name': 'Masha', 'age': 9, 'class': 'F'}]
```

#### Task 2.2
Moving average of a set of values and a window size is a series of local averages. You should
implement function, that calculate and return the moving average for the given list values of
integers. Integer n representing size of the window.
For example:
Values: [1, 2, 3, 4, 5]
Window size: 3
Moving average is calculated as:

• 1, 2, 3, 4, 5
| |
^^^^
(1+2+3)/3 = 2

• 1, 2, 3, 4, 5
 | |
 ^^^^^^
 (2+3+4)/3 = 3

• 1, 2, 3, 4, 5
 | |
 ^^^^^
 (3+4+5)/3 = 4

Here, the moving average would be [2, 3, 4] and function should return this list.

#### Task 2.3
Implement the function that returns true if it contains any duplicate argument values. Any number
of arguments may be passed into the function. The array values passed in will only be strings or
numbers. The only valid return values are true and false.

For example:
```python
>>> func(1, 2, 3)
False
>>> func (1, 2, 3, 2)
True
>>> func('1', '2', '3', '2')
True
```

#### Task 2.4*
Implement the decorator function, which helps to count how many times
the function has occurred.

NOTE: NOT able to use global variables.

Implementation example:
```python
@dec
def foo(): pass

foo()
foo()
foo()
foo()
r = foo()
print(r)
>>> 5
```


## Materials

#### Python Materials
* __Learning Python__, 4th Edition By Mark Lutz
* [Data structures](https://docs.python.org/3.6/tutorial/datastructures.html)
* [Variables and Types](https://www.learnpython.org/en/Variables_and_Types)
* __Basic__ Python tutorial from [here](https://www.tutorialspoint.com/python/index.htm)
* Very advanced [challenge](http://www.pythonchallenge.com/) for those who are bored