"""查找对应角色：一对一"""
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import pandas as pd
"""得到某个角色的信息"""


class FindRole:
    def __init__(self, role_name):
        self.role_name = role_name

    def findrole(self):
        role_things = pd.read_excel("C:/Users/YHT/Desktop/项目/原神各属性角色信息.xlsx", header=0, index_col=0)
        # 将属性所包含的nan，进行填充
        role_things = role_things.fillna(axis=0, method="ffill")
        print()
        all_name = role_things["角色"]
        num = 0
        for x in all_name:
            if x == self.role_name:
                return_role = role_things.loc[:, "属性":]
                return return_role.iloc[num]
            num+=1