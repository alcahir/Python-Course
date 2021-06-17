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

ACTIONS = {
            'price': FeatureTransformer.price_to_float,
            'date': FeatureTransformer.transform_date,
            'unixReviewTime': FeatureTransformer.transform_date,
           }


class DataParser:
    def __init__(self, path_to_json, num_rows):
        pass

    def get_data_iterator(self, path_to_data, num_rows):
        pass


    def get_rid_nested_data(self, row, nested_column):
        pass


    def upload_data(self, nested_key=None, updated_columns=[]):
        pass


    def to_DF(self):
        pass


    def save_data(self, saved_name='data.json'):
        pass

