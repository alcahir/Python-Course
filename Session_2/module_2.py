# from collections import defaultdict as dd
# from itertools import product
from typing import Any, Dict, List, Tuple


def task_1(data_1: Dict[str, int], data_2: Dict[str, int]):
    result = data_1.copy()

    for key, value in data_2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value

    return result


def task_2():
    return {i: i ** 2 for i in range(1, 16)}


def task_3(data: Dict[Any, List[str]]):
    result = ['']

    for values in data.values():
        new_result = []

        for prefix in result:
            for letter in values:
                new_result.append(prefix + letter)

        result = new_result

    return result


def task_4(data: Dict[str, int]):
    sorted_items = sorted(
        data.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return [key for key, _ in sorted_items[:3]]


def task_5(data: List[Tuple[Any, Any]]) -> Dict[str, List[int]]:
    result = {}

    for key, value in data:
        if key not in result:
            result[key] = []

        result[key].append(value)

    return result


def task_6(data: List[Any]):
    result = []

    for item in data:
        if item not in result:
            result.append(item)

    return result


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

    needle_len = len(needle)

    for i in range(len(haystack) - needle_len + 1):
        if haystack[i:i + needle_len] == needle:
            return i

    return -1
