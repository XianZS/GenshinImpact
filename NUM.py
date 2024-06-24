"""设置限制参数，查找对应角色：多对多"""
from pandas import DataFrame, Series
import pandas as pd
import numpy as np


class Num:
    def __init__(self, Hp, Def, Atk):
        self.Hp = Hp
        self.Def = Def
        self.Atk = Atk

    def num(self):
        role_things = pd.read_excel("C:/Users/YHT/Desktop/项目/原神各属性角色信息.xlsx", header=0, index_col=0)
        role_things = role_things.fillna(axis=0, method="ffill")
        if self.Hp is None:
            if self.Def is None:
                if self.Atk is None:
                    return role_things
                else:
                    return_things = role_things.loc[role_things["攻击力"] > self.Atk]
                    return return_things
            else:
                if self.Atk is None:
                    return_things = role_things.loc[role_things["防御力"] > self.Def]
                    return return_things
                else:
                    return_things = role_things.loc[
                        (role_things["防御力"] > self.Def) & (role_things["攻击力"] > self.Atk)]
                    return return_things
        else:
            if self.Def is None:
                if self.Atk is None:
                    return_things = role_things.loc[role_things["生命值"] > self.Hp]
                    return return_things
                else:
                    return_things = role_things.loc[
                        (role_things["生命值"] > self.Hp) & (role_things["攻击力"] > self.Atk)]
                    return return_things
            else:
                if self.Atk is None:
                    return_things = role_things.loc[
                        (role_things["生命值"] > self.Hp) & (role_things["防御力"] > self.Def)]
                    return return_things
                else:
                    return_things = role_things.loc[
                        (role_things["生命值"] > self.Hp) & (role_things["防御力"] > self.Def) & (
                                    role_things["攻击力"] > self.Atk)]
                    return return_things
