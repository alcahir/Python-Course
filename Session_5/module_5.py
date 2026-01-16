from collections import Counter
import os
from pathlib import Path
from random import choice
from random import seed
from typing import List, Union

import requests
from requests.exceptions import ConnectionError
from gensim.utils import simple_preprocess


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
        stop_words = set(
            word.strip().lower()
            for word in f
            if word.strip()
        )

    with open(PATH_TO_TEXT, "r", encoding="utf-8") as f:
        text = f.read()

    words = simple_preprocess(text, deacc=True)  # keeps only alphabetic, lowercase

    filtered_words = [word for word in words if word not in stop_words]

    counter = Counter(filtered_words)

    return counter.most_common(top_k)


from requests.exceptions import RequestException
import requests


def task3(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except RequestException:
        raise



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
        result = float(a) / float(b)
        print(result)
    except ZeroDivisionError:
        print("Can't divide by zero")
    except ValueError:
        print("Entered value is wrong")

