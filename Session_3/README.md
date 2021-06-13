## Tasks

#### Task 3.1
Open files __'names.txt'__ and __'last_names.txt'__. There are ~18000 names and approximately 98000 surnames.
Sort the names and make lowercase. __IMPORT__ from `random` method `choice`. 
You need to assign random surname to each name from __'names.txt'__ file and join them by __space__.
Whereupon, you have to write them to a new file called __'sorted_names_and_surnames.txt'__. 
Each name and surname should start with a new line as in the following example:

```python
aaisha zvorsky
aamir koelsch
...
zully coda
zulma akahi
```

#### Task 3.2
Write function `get_frequency_words(...)` with follow parameters:

* `path_to_text`;
* `path_to_stop words`;
* `top_number`.

Inside the function you need to open both __'random_text.txt'__ and __'stop_words.txt'__. 
Read the text from `random_text.txt` whereupon you need to delete stop words from text.
Finally, you have to print the top frequency of words. The number of printing words is the last parameter of function.

NOTE: words should only consist of alphabet tokens and be in lowercase.

```python
>>> get_frequency_words('random_text.txt', 'stop_words.txt', 5)
('far', 51)
('blind', 51)
('way', 51)
('Little', 50)
('Blind', 50)
```


#### Task 3.3

Implement the decorator function, which helps to count how many times
the function has occurred.

NOTE: __not__ able to use global variables.

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
* LEGB:
	- https://www.youtube.com/watch?v=QVdf0LgmICw&t=876s
	- Mark Lutz's "Learning Python 5th Edition" Chapter 17
* Files:
	- https://www.youtube.com/watch?v=Uh2ebFW8OYM
	- Mark Lutz's "Learning Python 5th Edition" Chapter 9. Files
* Import:
	- https://www.youtube.com/watch?v=CqvZ3vGoGs0
	- Mark Lutz's "Learning Python 5th Edition" Part V Chapters 22 -25




