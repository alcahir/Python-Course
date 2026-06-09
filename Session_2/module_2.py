# from collections import defaultdict as dd
# from itertools import product
from typing import Any, Dict, List, Tuple


def task_1(data_1: Dict[str, int], data_2: Dict[str, int]):
    r = {}
    for i in data_1.keys():
        if i in data_2.keys():
            r[i] = data_1[i] + data_2[i]
        else:
            r[i] = data_1[i]
    for i in data_2.keys():
        if i not in data_1.keys():
            r[i] = data_2[i]
    return r


def task_2():
    m = {}
    for i in range(1, 16):
        m[i] = i**2
    return m


def task_3(data: Dict[Any, List[str]]):
    a = ['']

    for b in data.values():
        c = []

        for x in a:
            for y in b:
                c.append(x + y)

        a = c

    return a


def task_4(data: Dict[str, int]):
    if data == {}:
        return []
    elif len(data) < 3:
        return list(data.keys())
    else:
        r = []
        max_values = data.values()  # finding 3 max values
        max_values = sorted(max_values, reverse=True)[:3]
        for i in data.keys():
            if data[i] in max_values:
                r.append(i)
    return r


def task_5(data: List[Tuple[Any, Any]]) -> Dict[str, List[int]]:
    d = {}
    for i in data:
        if i[0] in d.keys():
            d[i[0]].append(i[1])
        else:
            d[i[0]] = [i[1]]
    return d


def task_6(data: List[Any]):
    return list(set(data))


def task_7(words: [List[str]]) -> str:
    pass


def task_8(haystack: str, needle: str) -> int:
    pass
