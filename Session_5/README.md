
## Tasks

#### Task 1
Write a Python function `task_1` to open files __'names.txt'__ and __'last_names.txt'__. There are ~18000 names and approximately 98000 surnames.  
Sort the names and make lowercase. You need to assign random surname to each name by using `choice` function from `random` lib and join them by __space__.  
Whereupon, you have to write them to a new file called __'sorted_names_and_surnames.txt'__.  
Each name and surname should start with a new line as in the following example:  

```python
aadil contini
aaisha rion
aakash bitonti
aaliyah goettl
aamanda chartraw
...
zuleyka gruca
zully gracely
zulma porcaro
zvi brazzell
```

__USE THE DEFAULT PATHS FROM *.PY MODULE, PLEASE!__


#### Task 2
Write a Python function `task_2` with follow parameter:
* `top_k`.

Inside the function you need to open both `random_text.txt` and `stop_words.txt` files.   
Read the text from `random_text.txt`, whereupon you need to delete stop words in the text.  
Finally, you have to return list of tuples of the top words and frequency as well. The number of needed top words is the parameter of function.  
  
Note: words should only consist of alphabet tokens and be in lowercase.
```python
>>> task_2(5)
[('blind', 101), ('far', 68), ('text', 67), ('copy', 66), ('way', 51)]
```

__USE THE DEFAULT PATHS FROM *.PY MODULE, PLEASE!__

#### Task 3
Write Python function `task3` to get request by using given url. You need to raise an exception `RequestException` from `requests.exceptions`.  
Just info: It's a parent exception for `HTTPError`, `ConnectionError` and etc.  
Use the `response.raise_for_status()` to raise an exception.  
If your response has 200 status then just return `requests.get(url)` response.  

#### Task 4
Write a Python function `task_4` with parameter `data`. The data can contain such types of elements like `str`, `float`, `int`.  
You need to sum up all elements of `data` if it's possible. Otherwise you need to process exception `TypeError`.  
This exception should be able to convert strings to float.  
The function has to return the sum of the values in the list.  
Example:
```python
>>> get_sum([1, 2, 3])
6
>>> get_sum([1, '2', '3.5'])
6.5
```

#### Task 5
Write a Python function `task_5`. You need to declare two variables via `input().split()` in the body of the function.  
Try to divide first variable on second. If the second variable is zero you have to `print("Can't divide by zero")`.  
Another option is to `print("Entered value is wrong")`, if you get exception `ValueError`.  
Finally, if the result of division can be calculated without any exception then just print this result.


## Materials

#### Python Materials
* __Learning Python__, 4th Edition By Mark Lutz
  * _Chapter 33_ Exception Coding Details
  * _Chapter 35_ Designing with Exceptions
* [Exception handling](https://metanit.com/python/tutorial/2.11.php)



