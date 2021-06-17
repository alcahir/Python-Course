import pandas as pd
import numpy as np
import json
import csv
import argparse
import os
from copy import deepcopy
from collections import defaultdict as dd
from transformers import FeatureTransformer
from aggregate_functions import calculate_time

ACTIONS = {
            'price': FeatureTransformer.price_to_float,
            'date': FeatureTransformer.transform_date,
            'unixReviewTime': FeatureTransformer.transform_date,
           }


class DataParser:
    def __init__(self, path_to_json, num_rows):
        self.path_to_json = path_to_json
        self.num_rows = num_rows

    def get_data_iterator(self, path_to_data, num_rows):
        assert os.path.exists(path_to_data), "Incorrect path"

        with open(path_to_data) as read_file:
            for idx_row, row in enumerate(read_file):
                yield json.loads(row)

                if idx_row == num_rows - 1:
                    break


    def get_rid_nested_data(self, row, nested_column):
        flag = False
        if row.get(nested_column) != None:
            size_categories = len(row.get(nested_column))
            flag = True
        else:
            size_categories = 1

        for category_num in range(size_categories):
            copy_row = deepcopy(row)
            if flag == True:
                copy_row[nested_column] = row[nested_column][category_num]
            yield copy_row


    @calculate_time
    def upload_data(self, nested_key=None, updated_columns=[]):
        self.data = []
        for idx, row in enumerate(self.get_data_iterator(self.path_to_json, self.num_rows)):
            for unnested_row in self.get_rid_nested_data(row, nested_key):
                for key in updated_columns:
                    if unnested_row.get(key) != None:
                        unnested_row[key] = ACTIONS[key](unnested_row[key])
                self.data.append(unnested_row)


    def to_DF(self):
        df = {}
        for idx_row, row in enumerate(self.data):
            df[idx_row] = row
        self.data = pd.DataFrame.from_dict(df, orient='index')


    def save_data(self, saved_name='data.json'):
        saved_format = saved_name[saved_name.find('.') + 1:]

        if saved_format == "json":
            self.data.to_json(saved_name)

        if saved_format == "csv":
            self.data.to_csv(saved_name)

        if saved_format == 'pickle':
            self.data.to_pickle(saved_name)


if __name__ == '__main__':
    metadata = DataParser(
        'C:/Users/Egor_Pilat/Downloads/Python_task/meta_Industrial_and_Scientific/meta_Industrial_and_Scientific_updated.json',
        1000)
    reviews = DataParser(
        'C:/Users/Egor_Pilat/Downloads/Python_task/Industrial_and_Scientific/Industrial_and_Scientific_updated.json',
        1000)
    metadata.upload_data(nested_key='category', updated_columns=['price', 'date'])
    reviews.upload_data(updated_columns=['unixReviewTime'])
    reviews.to_DF()
    metadata.to_DF()
    metadata.save_data(saved_name = 'metadata.csv')
    reviews.save_data()