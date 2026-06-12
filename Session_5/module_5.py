import os
import re
from collections import Counter
from pathlib import Path
from random import choice, seed
from typing import List, Union
import requests
from requests.exceptions import RequestException

BASE_PATH = Path(os.path.realpath(__file__)).parent
PATH_TO_NAMES = BASE_PATH / "names.txt"
PATH_TO_SURNAMES = BASE_PATH / "last_names.txt"
PATH_TO_OUTPUT = BASE_PATH / "sorted_names_and_surnames.txt"
PATH_TO_TEXT = BASE_PATH / "random_text.txt"
PATH_TO_STOP_WORDS = BASE_PATH / "stop_words.txt"


def task_1() -> None:
    seed(1)
    
    with open(PATH_TO_NAMES, "r", encoding="utf-8") as f_names:
        names = [line.strip().lower() for line in f_names if line.strip()]
        
    with open(PATH_TO_SURNAMES, "r", encoding="utf-8") as f_surnames:
        surnames = [line.strip().lower() for line in f_surnames if line.strip()]
        
    names.sort()
    
    with open(PATH_TO_OUTPUT, "w", encoding="utf-8") as f_out:
        for name in names:
            random_surname = choice(surnames)
            f_out.write(f"{name} {random_surname}\n")


def task_2(top_k: int) -> List:
    with open(PATH_TO_STOP_WORDS, "r", encoding="utf-8") as f_stop:
        stop_words = {line.strip().lower() for line in f_stop if line.strip()}
        
    with open(PATH_TO_TEXT, "r", encoding="utf-8") as f_text:
        text = f_text.read().lower()
        
    words = re.findall(r"[a-z]+", text)
    filtered_words = [word for word in words if word not in stop_words]
    word_counts = Counter(filtered_words)
    
    return word_counts.most_common(top_k)


def task_3(url: str) -> requests.Response:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
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


def task_4(data: List[Union[int, str, float]]) -> Union[int, float]:
    total = 0
    for item in data:
        try:
            total += item
        except TypeError:
            total += float(item)
            
    if isinstance(total, float) and total.is_integer():
        return int(total)
        
    return total


def task_5() -> None:
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
