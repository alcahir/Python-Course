
## Tasks

#### Task 4.1
Implement an abstract class named `GeometricFigure()`. It should have abstract methods to calculate square
and perimeter of the figure.


#### Task 4.2
Implement class named `Circle()`. It must inherit abstract class `GeometricFigure` from __Task 4.1__. Instance of this
class is initialized by radius. It must have redefined methods of a parent class to calculate square and
perimeter of the circle.


#### Task 4.3
Write a function `start quiz()` which has 5 questions with boolean options of answer inside itself.
The first question "What's your name?" is without scoring.

Example of quesions:
* Do you like this course? (_Yes_ / _No_)
* Do you want the next session? :) (_Yes_ / _No_)
* Is carrot red? (_Yes_ / _No_)
* ...
* ...

The number of points for each question depends on your fancy.
Note: use `input()` function to provide an opportunity to give the answer.


#### Task 4.4* __Mini quiz__ 
Write a Python class named Student with two attributes `student_name` and `mark`.
Implement a magic method `__call__` so that when you call this method then will start the survey from __Task 4.3__.
The result of quiz and name of student have to be written in `mark` and `student_name` attributes of class. 
After printing an instance of this class, should be displayed a message __'Student {student_name} has received {mark} points'__.


## Materials

#### Python Materials
* __Learning Python__, 4th Edition By Mark Lutz
  * _Chapter 25_ OOP: The Big Picture
  * _Chapter 26_ Class coding Basics
  * _Chapter 29_ Operator Overloading
* [Abstract classes in Python](https://www.geeksforgeeks.org/abstract-classes-in-python/)



