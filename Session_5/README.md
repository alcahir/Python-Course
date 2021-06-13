
## Tasks

#### Task 5.1
Write a function `get_url(...)` that has only one parameter, namely __str: url__. 
If url constists of 'http' instead of 'https' then function has to `raise Exception('Unsecured protocol')`.
Otherwise, the function should print 'Secured protocol'

```python
>>> get_url('http://vacation.epam.com/')
Exception: Unsecured protocol
>>> get_url('https://vacation.epam.com/')
Secured protocol
```

#### Task 5.2
Write a function `get_sum(...)` with parameter __list: numbers__.
If __numbers__ contains numbers like strings you have to except __('TypeError')__. 
This exception should be able to convert strings to float.
The function has to return the sum of the values in the list.

Example:
```python
>>> get_sum([1, 2, 3])
6
>>> get_sum([1, '2', '3.5'])
7.5
```

#### Task 5.3
Write a function `divide_numbers()`.
You need to declare two variables via `input()` in the body of the function.
Try to divide first variable on second. If the second variable is zero you have to __print "Can't divide by zero"__.
Another option is to __print "Entered value is wrong" when you get `ValueError`.
Finally, if result of function doesn't have problems it has to return result of dividing.

NOTE: Look at `ZeroDivisionError`. you can use mulpiple exceptions.


## Materials

#### Python Materials
* __Learning Python__, 4th Edition By Mark Lutz
  * _Chapter 33_ Exception Coding Details
  * _Chapter 35 Designing with Exceptions
* [Exception handling](https://metanit.com/python/tutorial/2.11.php)



