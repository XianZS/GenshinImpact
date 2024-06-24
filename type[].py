"""绘图"""
from pyecharts.charts import Timeline
from find_type import FindType
import pandas as pd
from pyecharts.charts import Bar, Page
from pyecharts.charts import Scatter
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker


def a():
    return_things = FindType("冰").find_type()
    c = (
        Line()
        .add_xaxis(list(return_things["角色"]))
        .add_yaxis("生命值", list(return_things["生命值"]), is_connect_nones=True)
        .add_yaxis("防御力", list(return_things["防御力"]), is_connect_nones=True)
        .add_yaxis("攻击力", list(return_things["攻击力"]), is_connect_nones=True)
        .set_global_opts(title_opts=opts.TitleOpts(title="折线图"))
    )
    return c


def b():
    role_things = pd.read_excel("C:/Users/YHT/Desktop/项目/原神各属性角色信息.xlsx", header=0, index_col=0)
    role_things = role_things.fillna(axis=0, method="ffill")
    print(role_things)
    return_things = FindType("冰").find_type()
    df = return_things.drop(["属性", "突破加成"], axis=1)
    Name = df["角色"]
    Hp = df["生命值"]
    Def = df["防御力"]
    Atk = df["攻击力"]
    c = (
        Scatter()
        .add_xaxis(list(Name))
        .add_yaxis("生命值", list(Hp))
        .add_yaxis("防御力", list(Def))
        .add_yaxis("攻击力", list(Atk))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="冰属性"),
            visualmap_opts=opts.VisualMapOpts(type_="size", max_=150, min_=20),
            xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate": 45})
        )
    )
    return c


def c():
    return_things = FindType("冰").find_type()
    df = return_things.drop(["属性", "突破加成"], axis=1)
    list_source = [["produce", "生命值", "防御力", "攻击力"]]
    for x in range(0, len(df["角色"])):
        list_source.append([df.iloc[x]["角色"],
                            int(df.iloc[x]["生命值"]),
                            int(df.iloc[x]["防御力"]),
                            int(df.iloc[x]["攻击力"])])
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
            title_opts=opts.TitleOpts(title="冰属性"),
            xaxis_opts=opts.AxisOpts(type_="category"),
        )
    )
    return c


page = Page(layout=Page.DraggablePageLayout)
page.add(a(), b(), c())
# page.render(".html")
# Page.save_resize_html(".html", cfg_file="", dest="./templates/冰属性.html")