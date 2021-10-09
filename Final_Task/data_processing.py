#import pandas as pd
#import numpy as np
#import json
#import csv
#import argparse
#import os
#from copy import deepcopy
#rom collections import defaultdict as dd
#from transformers import FeatureTransformer
#from aggregate_functions import calculate_time
#from typing import List

ACTIONS = {
            'price': FeatureTransformer.price_to_float,
            'date': FeatureTransformer.transform_date,
            'unixReviewTime': FeatureTransformer.transform_date,
           }


class DataParser:
    def __init__(self, path_to_json, num_rows):
        self.path_to_json = path_to_json
        self.num_rows = num_rows
        self.parsed_data: List[dict] = []

    def get_data_iterator(self):
        if os.path.exists(self.path_to_json):
            ### Your code ###

        with open(self.path_to_json) as read_file:
            for row in read_file:
                ### your code ###


    def get_rid_nested_data(self, row, nested_column):
        if row.get(nested_column, False) or not isinstance(row[nested_column], list):
            raise NestedError('You have a problem with name of column or its not a list')

        for category in row[nested_column]:
            row_copy = deepcopy(row)
            ### Your code ###
            ### ... ###


    def upload_data(self, nested_key=None, updated_columns: list):
        for row in self.get_data_iterator():
            for unnested_row in self.get_rid_nested_data(row, nested_key):
                # Start your code
                # ...
                # End your code
                self.parsed_data.append(unnested_row)

        self.to_DF()


    def to_DF(self):
        ### your code ###


    def save_data(self, saved_name='data.json'):
        ### your code ###


class NestedError(Exception):
    pass


if __name__ == '__main__':
    doc_1 = DataParser(..., ...)
    doc_1.save_data(...)
    doc_2 = DataParser(..., ...)
    doc_2.save_data(...)