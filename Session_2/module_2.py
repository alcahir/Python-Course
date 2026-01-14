# from collections import defaultdict as dd
# from itertools import product
from typing import Any, Dict, List, Tuple


# from collections import defaultdict as dd
# from itertools import product
from typing import Any, Dict, List, Tuple


def task_1(data_1: Dict[str, int], data_2: Dict[str, int]):
    result = d1.copy()
    for key, value in d2.items():
        result[key] = result.get(key, 0) + value  
    return result
    


def task_2():
    return {i: i**2 for i in range(1, 16)}
    

from itertools import product
def task_3(data: Dict[Any, List[str]]):
    return [''.join(comb) for comb in product(*data.values())]


def task_4(data: Dict[str, int]):
    result = []
    for key in sorted(data, key=data.get, reverse=True):
        result.append(key)
        if len(result) == 3:
            break
    return result


def task_5(data: List[Tuple[Any, Any]]) -> Dict[str, List[int]]:
    
    result = {}
    
    for key, value in pairs:
        if key not in result:
            result[key] = []
        result[key].append(value)
    
    return result


def task_6(data: List[Any]):
    result = []
    
    for item in lst:
        if item not in result:
            result.append(item)
    
    return result


def task_7(words: [List[str]]) -> str:
    if not words:
        return ""
    
    prefix = words[0]
    
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    
    return prefix


def task_8(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    
    n, m = len(haystack), len(needle)
    
    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:
            return i
    
    return -1

