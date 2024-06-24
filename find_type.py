"""各元素角色信息：一对多"""
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
"""找到火属性角色"""

class FindType:
    # 自动执行，将传入参数赋值给私有属性self.Attribute
    def __init__(self, attribute):
        self.Attribute = attribute

    def find_type(self):
        role_things = pd.read_excel("C:/Users/YHT/Desktop/项目/原神各属性角色信息.xlsx", header=0, index_col=0)
        # 补全
        role_things = role_things.fillna(axis=0, method="ffill")
        # 按照"属性"这一列的信息，将所有数据重新分组，得到一个字典
        things_list = role_things.groupby("属性").groups
        return role_things.loc[things_list[self.Attribute]]
