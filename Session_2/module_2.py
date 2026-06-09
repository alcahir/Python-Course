from collections import defaultdict as dd
from itertools import product
from typing import Any, Dict, List, Tuple


def task_1(data_1: Dict[str, int], data_2: Dict[str, int]):
    result = dict(data_1)
    for key, value in data_2.items():
        result[key] = result.get(key, 0) + value
    return result


def task_2():
    return {i: i ** 2 for i in range(1, 16)}


def task_3(data: Dict[Any, List[str]]):
    return ["".join(combo) for combo in product(*data.values())]


def task_4(data: Dict[str, int]):
    sorted_keys = sorted(data, key=lambda k: data[k], reverse=True)
    return sorted_keys[:3]


def task_5(data: List[Tuple[Any, Any]]) -> Dict[str, List[int]]:
    result = dd(list)
    for key, value in data:
        result[key].append(value)
    return dict(result)


def task_6(data: List[Any]):
    seen = []
    for item in data:
        if item not in seen:
            seen.append(item)
    return seen


def task_7(words: List[str]) -> str:
    if not words:
        return ""
    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


def task_8(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    return haystack.find(needle)
