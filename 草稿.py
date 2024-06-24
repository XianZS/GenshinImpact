import pandas as pd

role_things = pd.read_excel("C:/Users/YHT/Desktop/项目/原神各属性角色信息.xlsx", header=0, index_col=0)
role_things = role_things.fillna(axis=0, method="ffill")
print(role_things["生命值"].mean(),type(role_things["生命值"].mean()))