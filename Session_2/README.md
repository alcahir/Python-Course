
## Tasks

#### Task 1
Write a Python function `task_1` to combine two dictionary adding values for common keys. Return updated dict.
```python
>>> task_1({'a': 123, 'b': 23, 'c': 0}, {'a': 1, 'b': 11, 'd': 99})
{'a': 124, 'b': 34, 'c': 0, 'd': 99}
```

#### Task 2
Write a Python function `task_2` to return a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.

#### Task 3
Write a Python function `task_3` to create and display all combinations of letters, selecting each letter from a different key in a dictionary.  
Return list of combinations.
```python
>>> task_3({'1': ['a', 'b'], '2': ['c', 'd']})
["ac", "ad", "bc", "bd"]
>>> task_3({'1': ['a', 'b'], '2': ['c', 'd'], '3': ['d', 'e']})
["acd", "ace", "add", "ade", "bcd", "bce", "bdd", "bde"]
```

#### Task 4
Write a Python function `task_4` to find the highest 3 values of corresponding keys in a dictionary.  
If dictionary contains less then 3 values, you need to return the remaining.  
Return List[aim elements].
```python
>>> task_4({'a': 500, 'b': 5874, 'c': 560,'d': 400, 'e': 5874, 'f': 20})
["b", "e", "c"]
>>> task_4({'a': -1})
['a']
>>> task_4({})
[]
```

#### Task 5
Write a Python function `task_5` to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.  
Original list:  
[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]  
Grouping a sequence of key-value pairs into a dictionary of lists:  
{'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}

### Optional

#### Task 6
Write a Python function `task_6` to delete repeated elements from list.
```python
>>> task_6([1, 1, 3, "3"]
[1, 3, "3"]
```

#### Task 7
Write a Python function `task_7` to find the longest common prefix string amongst an array of strings.  
If there is no common prefix, return an empty string "".  
```python
>>> task_7(["flower", "flows"])
flow
>>> task_7(["sun", "recap"])
""
```

#### Task 8
Write a Python function `task_8` to return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.  
What should we return when needle is an empty string?  
For the purpose of this problem, we will return 0 when needle is an empty string.
```python
>>> task_8("Star Killer", "Killer")
5
>>> task_8("Star Killer", "Miller")
-1
>>> task_8("Star Killer", "")
0
```

## Materials

#### Python Materials
* __Learning Python__, 4th Edition By Mark Lutz
* [Data structures](https://docs.python.org/3.6/tutorial/datastructures.html)
* [Variables and Types](https://www.learnpython.org/en/Variables_and_Types)
* __Basic__ Python tutorial from [here](https://www.tutorialspoint.com/python/index.htm)