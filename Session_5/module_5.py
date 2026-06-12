from collections import Counter
import os
from pathlib import Path
from random import choice
from random import seed
from typing import List, Union

import requests
from requests.exceptions import RequestException
import re

S5_PATH = Path(os.path.realpath(__file__)).parent

PATH_TO_NAMES = S5_PATH / "names.txt"
PATH_TO_SURNAMES = S5_PATH / "last_names.txt"
PATH_TO_OUTPUT = S5_PATH / "sorted_names_and_surnames.txt"
PATH_TO_TEXT = S5_PATH / "random_text.txt"
PATH_TO_STOP_WORDS = S5_PATH / "stop_words.txt"


def task_1():
    seed(1)

    with open(PATH_TO_NAMES, 'r', encoding='utf-8') as f:
        names = [name.strip().lower() for name in f]

    with open(PATH_TO_SURNAMES, 'r', encoding='utf-8') as f:
        surnames = [surname.strip().lower() for surname in f]

    names.sort()

    with open(PATH_TO_OUTPUT, 'w', encoding='utf-8') as f:
        for name in names:
            f.write(f'{name} {choice(surnames)}\n')


def task_2(top_k: int):
    with open(PATH_TO_STOP_WORDS, 'r', encoding='utf-8') as f:
        stop_words = set(word.strip().lower() for word in f)

    with open(PATH_TO_TEXT, 'r', encoding='utf-8') as f:
        text = f.read().lower()

    words = re.findall(r'[a-z]+', text)

    words = [word for word in words if word not in stop_words]

    counter = Counter(words)

    return counter.most_common(top_k)


def task_3(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except RequestException:
        raise


def task_4(data: List[Union[int, str, float]]):
    try:
        return sum(data)
    except TypeError:
        return sum(float(x) for x in data)


def task_5():
    try:
        a, b = input().split()
        print(float(a) / float(b))
    except ZeroDivisionError:
        print("Can't divide by zero")
    except ValueError:
        print("Entered value is wrong")
