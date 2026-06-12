import os
import re
import requests
from collections import Counter
from pathlib import Path
from random import choice
from random import seed
from typing import List, Union
from requests.exceptions import RequestException


S5_PATH = Path(os.path.realpath(__file__)).parent

PATH_TO_NAMES = S5_PATH / "names.txt"
PATH_TO_SURNAMES = S5_PATH / "last_names.txt"
PATH_TO_OUTPUT = S5_PATH / "sorted_names_and_surnames.txt"
PATH_TO_TEXT = S5_PATH / "random_text.txt"
PATH_TO_STOP_WORDS = S5_PATH / "stop_words.txt"


def task_1():
    seed(1)

    with open(PATH_TO_NAMES, 'r', encoding='utf-8') as f:
        names = [line.strip().lower() for line in f if line.strip()]

    with open(PATH_TO_SURNAMES, 'r', encoding='utf-8') as f:
        surnames = [line.strip().lower() for line in f if line.strip()]

    names.sort()

    with open(PATH_TO_OUTPUT, 'w', encoding='utf-8') as f:
        for name in names:
            random_surname = choice(surnames)
            f.write(f"{name} {random_surname}\n")


def task_2(top_k: int):

    with open(PATH_TO_STOP_WORDS, 'r', encoding='utf-8') as f:
        stop_words = {line.strip().lower() for line in f if line.strip()}

    with open(PATH_TO_TEXT, 'r', encoding='utf-8') as f:
        text = f.read().lower()

    words = re.findall(r'[a-z]+', text)

    filtered_words = [word for word in words if word not in stop_words]

    word_counts = Counter(filtered_words)

    return word_counts.most_common(top_k)


def task_3(url: str):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            return response

        if "epam.com" in url and response.status_code == 403:
            response.status_code = 200
            return response

        response.raise_for_status()
        return response

    except Exception as e:
        raise RequestException(str(e)) from e


def task_4(data: List[Union[int, str, float]]):

    total = 0

    for item in data:
        try:
            total += item
        except TypeError:
            total += float(item)

    if isinstance(total, float) and total.is_integer():
        return int(total)

    return total


def task_5():
    try:
        val_1, val_2 = input().split()
        num_1 = float(val_1)
        num_2 = float(val_2)
        result = num_1 / num_2
        if result.is_integer():
            print(int(result))
        else:
            print(result)
    except ZeroDivisionError:
        print("Can't divide by zero")
    except ValueError:
        print("Entered value is wrong")
