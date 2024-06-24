"""绘图"""
from pyecharts.charts import Scatter
from pyecharts import options as opts
from pyecharts.charts import Funnel
from pyecharts.faker import Faker
from pyecharts.charts import Bar
from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline
from pyecharts.faker import Faker
import numpy as np
import pandas as pd
from pyecharts.options import ToolboxOpts


# 散点图
class WriteScatter:
    Name = None
    Hp = None
    Def = None
    Atk = None

    def __init__(self, Name, Hp, Def, Atk):
        self.Name = Name
        self.Hp = Hp
        self.Def = Def
        self.Atk = Atk

    def write_scatter(self):
        from pyecharts.faker import Faker

        c = (
            Scatter()
            .add_xaxis(list(self.Name))
            .add_yaxis("生命值", list(self.Hp))
            .add_yaxis("防御力", list(self.Def))
            .add_yaxis("攻击力", list(self.Atk))
            .set_global_opts(
                toolbox_opts=ToolboxOpts(is_show=True),
                title_opts=opts.TitleOpts(title="数据显示-浮点图"),
                visualmap_opts=opts.VisualMapOpts(type_="size", max_=150, min_=20),
                xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate": 45})
            )
            .render("./templates/筛选结果-自动生成.html")
        )


# 漏斗图
class WriteFunnel:
    # 角色名称
    role_name = None
    # 分类依据
    type_things = None

    def __init__(self, role_name, type_things):
        self.role_name = role_name
        self.type_things = type_things

    # zip()函数
    # >>> a = ['a', 'b', 'c', 'd']
    # >>> b = ['1', '2', '3', '4']
    # >>> list(zip(a, b))
    # [('a', '1'), ('b', '2'), ('c', '3'), ('d', '4')]
    def write_funnel(self):
        c = (
            Funnel()
            .add(
                self.type_things,
                [list(z) for z in zip(self.role_name, self.type_things)],
                sort_="ascending",
                label_opts=opts.LabelOpts(position="inside"),
            )
            .set_global_opts(toolbox_opts=ToolboxOpts(is_show=True),
                             title_opts=opts.TitleOpts(title="数据显示-漏斗图"))
            .render("./templates/排序结果-自动生成.html")
        )


# 数据集
class WriteBarData:
    def __init__(self, df):
        self.df = df

    def write_bar_data(self):
        list_source = [["produce", "生命值", "防御力", "攻击力"]]
        for x in range(0, len(self.df["角色"])):
            list_source.append([self.df.iloc[x]["角色"],
                                int(self.df.iloc[x]["生命值"]),
                                int(self.df.iloc[x]["防御力"]),
                                int(self.df.iloc[x]["攻击力"])])
        print(list_source)
        c = (
            Bar()
            .add_dataset(
                source=list_source
            )
            .add_yaxis(series_name="生命值", y_axis=[])
            .add_yaxis(series_name="防御力", y_axis=[])
            .add_yaxis(series_name="攻击力", y_axis=[])
            .set_global_opts(
                toolbox_opts=ToolboxOpts(is_show=True),
                title_opts=opts.TitleOpts(title="数据集"),
                xaxis_opts=opts.AxisOpts(type_="category"),
            )
            .render("./templates/数据集-自动生成.html")
        )


# 饼图
class WritePie:
    def __init__(self, three_things, role_type, role_add):
        self.role_things = three_things
        self.role_type = role_type
        self.role_add = role_add

    def write_pie(self):
        print()
        print(self.role_things)
        c = (
            Pie()
            .add(
                "",
                # 这块可以是Series和Series，但不能是Series和list，因为两者无法匹配
                [list(z) for z in zip(["生命值", "防御力", "攻击力"],
                                      [int(self.role_things[0]), int(self.role_things[1]), int(self.role_things[2])])],
                radius=["40%", "75%"],
            )
            .set_global_opts(
                toolbox_opts=ToolboxOpts(is_show=True),
                title_opts=opts.TitleOpts(title=f"{self.role_type}属性角色/{self.role_add}"),
                legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
            )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            .render("./templates/单个角色数据-自动生成.html")
        )


# 时间柱状图
class WriteLineBar:
    def __init__(self):
        self.role_name = ["火", "水", "冰", "风", "雷", "岩"]

    def write_lin_bar(self):
        tl = Timeline()
        for i in self.role_name:
            role_things = pd.read_excel("C:/Users/YHT/Desktop/项目/原神各属性角色信息.xlsx", header=0, index_col=0)
            role_things = role_things.fillna(axis=0, method="ffill")
            things_list = role_things.groupby("属性").groups
            print(role_things.loc[things_list[i]]["角色"])
            bar = (
                Bar()
                .add_xaxis(list(role_things.loc[things_list[i]]["角色"]))
                .add_yaxis("生命值", list(role_things.loc[things_list[i]]["生命值"]))
                .add_yaxis("防御力", list(role_things.loc[things_list[i]]["防御力"]))
                .add_yaxis("攻击力", list(role_things.loc[things_list[i]]["攻击力"]))
                .set_global_opts(toolbox_opts=ToolboxOpts(is_show=True), title_opts=opts.TitleOpts(title="时间柱状图"))
            )
            tl.add(bar, f"{i}属性")
            tl.render("./templates/时间柱状图所有角色-自动生成.html")


# max和min对比图
class WriteMaxMim:
    def __init__(self):
        pass

    def write_max_min(self):
        from pyecharts import options as opts
        from pyecharts.charts import Bar
        from pyecharts.faker import Faker

        c = (
            Bar()
            .add_xaxis(Faker.choose())
            .add_yaxis("商家A", Faker.values())
            .add_yaxis("商家B", Faker.values())
            .set_global_opts(toolbox_opts=ToolboxOpts(is_show=True),
                             title_opts=opts.TitleOpts(title="max and min", subtitle="分析"))
            .render("")
        )
