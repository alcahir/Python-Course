"""
Module for preparing inverted indexes based on uploaded documents
"""
import json
import os
import re
import sys
from argparse import ArgumentParser, ArgumentTypeError, FileType
from io import TextIOWrapper
from typing import Dict, List, Set

DEFAULT_PATH_TO_STORE_INVERTED_INDEX = "inverted.index"


class EncodedFileType(FileType):
    """File encoder"""

    def __call__(self, string):
        # the special argument "-" means sys.std{in,out}
        if string == "-":
            if "r" in self._mode:
                stdin = TextIOWrapper(
                    sys.stdin.buffer, encoding=self._encoding
                )
                return stdin
            if "w" in self._mode:
                stdout = TextIOWrapper(
                    sys.stdout.buffer, encoding=self._encoding
                )
                return stdout
            msg = 'argument "-" with mode %r' % self._mode
            raise ValueError(msg)

        # all other arguments are used as file names
        try:
            return open(
                string,
                self._mode,
                self._bufsize,
                self._encoding,
                self._errors,
            )
        except OSError as exception:
            args = {"filename": string, "error": exception}
            message = "can't open '%(filename)s': %(error)s"
            raise ArgumentTypeError(message % args)

    def print_encoder(self):
        """printer of encoder"""
        print(self._encoding)


class InvertedIndex:
    """
    This module is necessary to extract inverted indexes from documents.
    """

    def __init__(self, words_ids: Dict[str, List[int]]):
        self.words_ids = words_ids

    def query(self, words: List[str]) -> List[int]:
        """Return the list of relevant documents for the given query"""
        if not words:
            return []
        result = None
        for word in words:
            word = word.lower().strip()
            if not word:
                continue

            doc_set = set(self.words_ids.get(word, []))

            if not doc_set and any(c for c in re.split(r"\W+", word) if c):
                sub_tokens = [t for t in re.split(r"\W+", word) if t]
                sub_result = None
                for token in sub_tokens:
                    token_set = set(self.words_ids.get(token, []))
                    if sub_result is None:
                        sub_result = token_set
                    else:
                        sub_result = sub_result & token_set
                doc_set = sub_result if sub_result else set()

            if result is None:
                result = doc_set
            else:
                result = result & doc_set

        return sorted(result) if result else []

    def dump(self, filepath: str) -> None:
        """
        Allow us to write inverted indexes documents to temporary directory
        or local storage
        :param filepath: path to file with documents
        :return: None
        """
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.words_ids, f)

    @classmethod
    def load(cls, filepath: str):
        """
        Allow us to upload inverted indexes from either temporary directory
        or local storage
        :param filepath: path to file with documents
        :return: InvertedIndex
        """
        with open(filepath, "r", encoding="utf-8") as f:
            words_ids = json.load(f)

        return cls(words_ids)


def load_documents(filepath: str) -> Dict[int, str]:
    """
    Allow us to upload documents from either tempopary directory
    or local storage
    :param filepath: path to file with documents
    :return: Dict[int, str]
    """
    documents = {}
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or "\t" not in line:
                continue
            try:
                doc_id_str, content = line.split("\t", 1)
                doc_id = int(doc_id_str.strip())
                documents[doc_id] = content.lower()
            except (ValueError, IndexError):
                continue

    return documents


def load_stop_words(filename: str = "stop_words_en.txt") -> Set[str]:
    """
    Dynamically locates and loads stop words relative to this script
    to delete them from document in later.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_dir, filename)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return {line.strip().lower() for line in f if line.strip()}
    except FileNotFoundError:
        # Prints a visible warning to the error stream without crashing
        print(
            f"Warning: Stop words file '{filename}' not found at {filepath}. "
            "Continuing without stop words.",
            file=sys.stderr,
        )
        return set()


def build_inverted_index(documents: Dict[int, str]) -> InvertedIndex:
    """
    Builder of inverted indexes based on documents
    :param documents: dict with documents
    :return: InvertedIndex class
    """
    words_ids: Dict[str, List[int]] = {}
    stop_words = load_stop_words("stop_words_en.txt")

    for doc_id, content in documents.items():
        words = re.split(r"\W+", content)
        for word in words:
            if not word:
                continue

            cleaned_word = word.lower().strip()

            if cleaned_word in stop_words:
                continue

            if cleaned_word not in words_ids:
                words_ids[cleaned_word] = []
            if doc_id not in words_ids[cleaned_word]:
                words_ids[cleaned_word].append(doc_id)

    return InvertedIndex(words_ids)


def callback_build(arguments) -> None:
    """process build runner"""
    return process_build(arguments.dataset, arguments.output)


def process_build(dataset, output) -> None:
    """
    Function is responsible for running of a pipeline to load documents,
    build and save inverted index.
    :param arguments: key/value pairs of arguments from 'build' subparser
    :return: None
    """
    documents: Dict[int, str] = load_documents(dataset)
    inverted_index = build_inverted_index(documents)
    inverted_index.dump(output)


def callback_query(arguments) -> None:
    """ "callback query runner"""
    process_query(arguments.query, arguments.index)


def process_query(queries, index) -> None:
    """
    Function is responsible for loading inverted indexes
    and printing document indexes for key words from arguments.query
    :param arguments: key/value pairs of arguments from 'query' subparser
    :return: None
    """
    inverted_index = InvertedIndex.load(index)
    stop_words = load_stop_words("stop_words_en.txt")  # Load the file here

    if not isinstance(queries, list):
        for line in queries:
            line = line.strip()
            if not line:
                continue

            # Filter out stop words from the file queries
            words = [
                w
                for w in re.split(r"\W+", line.lower())
                if w and w not in stop_words
            ]
            if not words:
                continue

            doc_ids = inverted_index.query(words)
            print(",".join(str(doc_id) for doc_id in doc_ids))

    else:
        for query_list in queries:
            # Filter out stop words from the command-line arguments
            words = [
                w.lower()
                for w in query_list
                if w.strip() and w.lower() not in stop_words
            ]
            if not words:
                continue
            doc_ids = inverted_index.query(words)
            print(",".join(str(doc_id) for doc_id in doc_ids))


def setup_subparsers(parser) -> None:
    """
    Initial subparsers with arguments.
    :param parser: Instance of ArgumentParser
    """
    subparser = parser.add_subparsers(dest="command")
    build_parser = subparser.add_parser(
        "build",
        help="this parser is need to load, build "
        "and save inverted index bases on documents",
    )
    build_parser.add_argument(
        "-d",
        "--dataset",
        required=True,
        help="You should specify path to file with documents. ",
    )
    build_parser.add_argument(
        "-o",
        "--output",
        default=DEFAULT_PATH_TO_STORE_INVERTED_INDEX,
        help="You should specify path to save inverted index. ",
    )
