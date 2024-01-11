# from collections import Counter
import os
from pathlib import Path
# from random import choice
from random import seed
from typing import List, Union

# import requests
# from requests.exceptions import ConnectionError
# from gensim.utils import simple_preprocess


S5_PATH = Path(os.path.realpath(__file__)).parent

PATH_TO_NAMES = S5_PATH / "names.txt"
PATH_TO_SURNAMES = S5_PATH / "last_names.txt"
PATH_TO_OUTPUT = S5_PATH / "sorted_names_and_surnames.txt"
PATH_TO_TEXT = S5_PATH / "random_text.txt"
PATH_TO_STOP_WORDS = S5_PATH / "stop_words.txt"


def task_1():
    seed(1)
    pass


def task_2(top_k: int):
    pass


def task_3(url: str):
    pass


def task_4(data: List[Union[int, str, float]]):
    pass


def task_5():
    pass
