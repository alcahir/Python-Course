from typing import List


def task_1(array: List[int], target: int) -> List[int]:
    seen = {} 

    for i, num in enumerate(array):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []


def task_2(number: int) -> int:
    result = 0
    
    while n > 0:
        digit = n % 10
        result = result * 10 + digit
        n //= 10
    
    return result


def task_3(array: List[int]) -> int:
   for x in nums:
        idx = abs(x) - 1
        if nums[idx] < 0:
            return abs(x)
        nums[idx] = -nums[idx]
    return -1


def task_4(string: str) -> int:
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in s:
        value = roman_map[char]
        if value > prev_value:
            # Subtraction case: remove the previously added value and add the difference
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value
    
    return total


def task_5(array: List[int]) -> int:
    if not nums:
        raise ValueError("List is empty")
    
    smallest = nums[0]  # start with the first element
    
    for num in nums[1:]:
        if num < smallest:
            smallest = num
            
    return smallest
