# from collections import defaultdict as dd
# from itertools import product
from typing import Any, Dict, List, Tuple


def task_1(data_1: Dict[str, int], data_2: Dict[str, int]):
    result = {}
    for x, y in data_1.items():
        if x in data_2:
            result.update({x: y + data_2.get(x)})
        else:
            result.update({x: y})
    for a, b in data_2.items():
        if a not in data_1:
            result.update({a: b})

    return result


def task_2():
    return {i: i ** 2 for i in range(1, 16)}


def task_3(data: Dict[Any, List[str]]):

    groups = list(data.values())  # [['a', 'b'], ['c', 'd']]

    result = [""]

    for group in groups:

        new_result = []  # [a, b]

        for prefix in result:

            for letter in group:

                new_result.append(prefix + letter)

        result = new_result

    return result


def task_4(data: Dict[str, int]):
    sorted_keys = sorted(data, key=data.get, reverse=True)
    return sorted_keys[:3]


def task_5(data: List[Tuple[Any, Any]]) -> Dict[str, List[int]]:
    result = {}

    for key, value in data:
        if key not in result:
            result[key] = []

        result[key].append(value)

    return result


def task_6(data: List[Any]):

    result = []

    seen = set()

    for item in data:

        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


def task_7(words: [List[str]]) -> str:
    words.sort()

    first = words[0]
    last = words[-1]

    longest_prefix = []

    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            longest_prefix.append(first[i])
        else:
            break

    return "".join(longest_prefix)


def task_8(haystack: str, needle: str) -> int:
    if needle == "":
        return 0

    return haystack.find(needle)
