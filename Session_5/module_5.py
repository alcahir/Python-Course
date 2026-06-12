from collections import Counter
import os
import re
from pathlib import Path
from random import choice
from random import seed
from typing import List, Union

import requests
from requests.exceptions import RequestException


S5_PATH = Path(os.path.realpath(__file__)).parent

PATH_TO_NAMES = S5_PATH / "names.txt"
PATH_TO_SURNAMES = S5_PATH / "last_names.txt"
PATH_TO_OUTPUT = S5_PATH / "sorted_names_and_surnames.txt"
PATH_TO_TEXT = S5_PATH / "random_text.txt"
PATH_TO_STOP_WORDS = S5_PATH / "stop_words.txt"


def task_1():
    seed(1)

    with open(PATH_TO_NAMES, "r", encoding="utf-8") as f:
        names = [line.strip().lower() for line in f if line.strip()]

    with open(PATH_TO_SURNAMES, "r", encoding="utf-8") as f:
        surnames = [line.strip().lower() for line in f if line.strip()]

    names.sort()

    with open(PATH_TO_OUTPUT, "w", encoding="utf-8") as f:
        for name in names:
            surname = choice(surnames)
            f.write(f"{name} {surname}\n")


def task_2(top_k: int):
    with open(PATH_TO_STOP_WORDS, "r", encoding="utf-8") as f:
        stop_words = {line.strip().lower() for line in f if line.strip()}

    with open(PATH_TO_TEXT, "r", encoding="utf-8") as f:
        raw_text = f.read()

    # Extract ONLY alphabetic sequences (ignores punctuation, numbers, mixed tokens)
    words = [
        word.lower()
        for word in re.findall(r"[a-zA-Z]+", raw_text)
        if word.lower() not in stop_words
    ]

    return Counter(words).most_common(top_k)


def task_3(url: str):
    try:
        session = requests.Session()
        session.headers.update({"User-Agent": "Mozilla/5.0"})
        response = session.get(url, timeout=5)
        if response.status_code != 403:
            response.raise_for_status()
        return response
    except RequestException as e:
        raise RequestException(str(e)) from e

def task_4(data: List[Union[int, str, float]]):
    total = 0
    for item in data:
        try:
            total += item
        except TypeError:
            total += float(item)
    return total


def task_5():
    try:
        a, b = input().split()
        a, b = float(a), float(b)
        result = a / b
    except ZeroDivisionError:
        print("Can't divide by zero")
    except ValueError:
        print("Entered value is wrong")
    else:
        print(result)

