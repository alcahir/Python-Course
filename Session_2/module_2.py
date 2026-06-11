from typing import List


def task_1(d1: dict, d2: dict) -> dict:
    merged = d1.copy()
    for k, v in d2.items():
        if k in merged:
            merged[k] += v
        else:
            merged[k] = v
    return merged


def task_2() -> dict:
    squares = {}
    for n in range(1, 16):
        squares[n] = n * n
    return squares


def task_3(d: dict) -> List[str]:
    combos = ['']
    for chars in d.values():
        combos = [existing + ch for existing in combos for ch in chars]
    return combos


def task_4(d: dict) -> List[str]:
    if not d:
        return []
    ranked = sorted(d, key=lambda x: d[x], reverse=True)
    return ranked[:3]


def task_5(pairs: list) -> dict:
    grouped = {}
    for k, v in pairs:
        if k in grouped:
            grouped[k].append(v)
        else:
            grouped[k] = [v]
    return grouped


def task_6(lst: list) -> list:
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique


def task_7(strs: List[str]) -> str:
    if not strs:
        return ""
    common = strs[0]
    for word in strs[1:]:
        while not word.startswith(common):
            common = common[:-1]
            if not common:
                return ""
    return common


def task_8(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1