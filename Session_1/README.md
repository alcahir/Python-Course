## Task 1
Once upon a time, there was a little mathematician named Lily who loved solving puzzles. One day, she came across a special puzzle.
In this puzzle, Lily was given a magical list of numbers, and she had to find a special pair of numbers that, when added together, gave a specific answer. The puzzle also told her the target sum she needed to find.
Lily's mission is to search the list and find those two magical numbers.

Can you help Lily to solve this task?

##### _Input:_
List of integers
```python
sample = [3, 4, -1, 10, 12]
target = 2
```
##### _Output:_
Pair in list
```python
[3, -1]
```

##### _Notes:_
- If the puzzle can __NOT__ be solved you need to return empty list.
- It is guaranteed that there can be at most one pair in the puzzle that gives the target sum.

##### _Restrictions:_
* Nested loops are forbidden
```python
for ...:
    for ...
```
![bear](https://github.com/alcahir/Python-Course/assets/57391255/862e9e9e-e585-4cda-828a-898b4eb27fa4)


## Task 2
In a magical land called the Land of Mirrors, there lived a young explorer named Lily. Lily was fascinated by the wonders of reflection and loved to solve number mysteries.
In the Land of Mirrors, flipping an integer was an enchanting process. It involved placing the number in front of a magical mirror, which would reflect and rearrange the digits, creating a new number with the digits in reverse order. It was like a magical dance of numbers!
Excited to uncover the secrets of the Land of Mirrors, Lily took hold of a number and approached a magnificent mirror. With a gleam in her eyes, Lily placed the number in front of the mirror and watched in amazement as the reflection rearranged the digits, creating a new number.
For example, if Lily placed the number 123 in front of the mirror, the reflection would transform it into the number 321.

Can you help Lily to solve the task?

##### _Input:_
List of integers
```python
sample = 130
```
##### _Output:_
```python
31
```

##### _Restrictions:_
* Using string operations are strictly forbidden.

![tom](https://github.com/alcahir/Python-Course/assets/57391255/f13d1cf9-7e46-4581-8eac-ec2689ada29d)


## Task 3
In a colorful world of numbers, there was a young adventurer named Max. Max loved embarking on exciting quests and solving a number of mysteries. One day, Max encountered a special challenge.
In this extraordinary challenge, Max was given a magical list of integers between 1 and n inclusively, where the n - length of the input list. He was asked to find the first number that appeared more than once on the list(where the list is read from left to right).

Can you help Max to solve this task?

##### _Input:_
List of integers
```python
sample = [2, 1, 3, 4, 2]
```
##### _Output:_
```python
2
```
##### _Notes:_
- If no one integer appears more than once you need to return -1.
- Try to solve the task witohut additional containers, sush as, list, dict, set and etc.
##### _Restrictions:_
* Method `.index` is also forbidden
```python
[1,2,3,].index(2) (no-no-no)
```
![aki](https://github.com/alcahir/Python-Course/assets/57391255/ac2fbfc5-0a6d-40db-976c-63fb16552270)


## Task 4

In a distant kingdom, there lived a young scholar named Mia who had a deep love for history and ancient civilizations. Mia was fascinated by the mysterious world of Rome and its numerical system. One day, Mia encountered a special challenge.
In this enchanting task, Mia was presented with magical symbols from ancient Rome. These symbols represented numbers, but they were different from the familiar digits Mia was accustomed to. Mia's mission was to convert these Roman symbols into regular numbers.

Let's try to solve the task!

##### _Notes:_
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
It is guaranteed that only the mentioned characters will be suppressed on the input.

| Symbol | Value |
| ------ | ------ |
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. 
Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. 
There are six instances where subtraction is used:

* `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 
* `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
* `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

##### _Input:_
```python
sample = "XIX"
```
##### _Output:_
```python
19
```

## Task 5
In a whimsical land filled with numbers, there lived a young mathematician named Leo. Leo had a passion for finding treasures hidden within numerical realms. One day, Leo stumbled upon a captivating challenge.
In this magical task, Leo was presented with a list of integers. The quest was to find the smallest number among them, like a precious gem waiting to be discovered.

It's worth a try!

##### _Input:_
List of integers
```python
sample = [3, 4, -1, 10, 12]
```
##### _Output:
```python
-1
```
##### _Restrictions:_
* Usage of `min` function is forbidden
```python
min(sample) (🦨-🦨-🦨)
```
