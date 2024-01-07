import os
import sys
from unittest.mock import patch

from final_task import main, process_build, process_query

PATH_TO_JSON_INDEX = "inverted.index"
PATH_TO_SIMPLE_QUERIES = "simple_queries.txt"
PATH_TO_DATASET = "wikipedia_sample"


def test_process_build_inverted_indexes():
    if os.path.exists(PATH_TO_JSON_INDEX):
        os.remove(PATH_TO_JSON_INDEX)

    process_build(
        dataset=PATH_TO_DATASET,
        output=PATH_TO_JSON_INDEX,
    )
    assert os.path.exists(PATH_TO_JSON_INDEX), "file is not defined"


def test_process_query_can_process_all_queries_from_file(capsys):
    with open(PATH_TO_SIMPLE_QUERIES) as queries_file:
        process_query(
            queries=queries_file,
            index=PATH_TO_JSON_INDEX,
        )
        captured = capsys.readouterr()

        for value in ["8522", "8716", "4086"]:
            assert value in captured.out


def test_std_argv_input_query(capsys):
    with patch.object(sys, "argv", ["prog", "query", "--query", "python", "code"]):
        main()

    out, err = capsys.readouterr()

    for value in [6021, 2581, 5783, 7575, 8864, 4266, 6698, 5295, 6834, 9010]:
        assert str(value) in out
