"""按照某一参数重新排序：一对多"""
from pandas import DataFrame, Series
import pandas as pd
import numpy as np


class Sort:
    def __init__(self, input_x,role_thing):
        self.input_x = input_x
        self.role_thing=role_thing
    def sort(self):
        type_bool = True
        print(self.input_x)
        role_things = self.role_thing.fillna(axis=0, method="ffill")
        print(type(role_things))
        return_things = role_things.sort_values(self.input_x, ascending=type_bool, axis=0)
        return return_things
