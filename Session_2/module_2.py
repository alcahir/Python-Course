# from collections import defaultdict as dd
# from itertools import product
from typing import Any, Dict, List, Tuple


def task_1(data_1: Dict[str, int], data_2: Dict[str, int]) -> Dict[str, int]:
    """
    Combine two dictionaries, adding values for common keys.
    """
    result = dict(data_1)  # copy so we don't mutate input
    for k, v in data_2.items():
        result[k] = result.get(k, 0) + v
    return result


def task_2() -> Dict[int, int]:
    """
    Return dict with keys 1..15 and values = key^2.
    """
    return {i: i * i for i in range(1, 16)}


def task_3(data: Dict[Any, List[str]]) -> List[str]:
    """
    Create all combinations of letters, taking one letter from each key's list.
    Order is based on insertion order of keys in the dict.
    """
    if not data:
        return []

    keys = list(data.keys())
    result: List[str] = []

    def backtrack(i: int, current: str) -> None:
        if i == len(keys):
            result.append(current)
            return
        for ch in data[keys[i]]:
            backtrack(i + 1, current + ch)

    backtrack(0, "")
    return result


def task_4(data: Dict[str, int]) -> List[str]:
    """
    Return keys of the highest 3 values. If < 3 items, return as many as exist.
    If values tie, order between tied keys follows the dict insertion order.
    """
    if not data:
        return []
    # Python sort is stable, so ties keep original insertion order
    top = sorted(data.items(), key=lambda kv: kv[1], reverse=True)[:3]
    return [k for k, _ in top]


def task_5(data: List[Tuple[Any, Any]]) -> Dict[Any, List[Any]]:
    """
    Group a sequence of (key, value) pairs into dict of lists.
    """
    grouped: Dict[Any, List[Any]] = {}
    for k, v in data:
        if k not in grouped:
            grouped[k] = []
        grouped[k].append(v)
    return grouped


def task_6(data: List[Any]) -> List[Any]:
    """
    Delete repeated elements from list, keeping first occurrences (stable order).
    """
    seen = set()
    result = []
    for x in data:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


def task_7(words: List[str]) -> str:
    """
    Find the longest common prefix among strings.
    """
    if not words:
        return ""

    prefix = words[0]
    for w in words[1:]:
        # shrink prefix until it matches the start of w
        while not w.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix


def task_8(haystack: str, needle: str) -> int:
    """
    Return index of first occurrence of needle in haystack, or -1.
    If needle is empty, return 0.
    """
    if needle == "":
        return 0

    n, m = len(haystack), len(needle)
    if m > n:
        return -1

    for i in range(n - m + 1):
        if haystack[i : i + m] == needle:
            return i
    return -1
