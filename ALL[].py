"""绘图"""
from pyecharts.charts import Timeline
from pyecharts.options import ToolboxOpts

from find_type import FindType
import pandas as pd
from pyecharts.charts import Bar, Page
from pyecharts import options as opts
from pyecharts.charts import Scatter


# 全部角色
def x():
    tl = Timeline()
    for i in ["火", "水", "冰", "风", "雷", "岩"]:
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
            .set_global_opts(toolbox_opts=ToolboxOpts(is_show=True), title_opts=opts.TitleOpts())
        )
        tl.add(bar, f"{i}属性")
    return tl


# 火
def y():
    return_things = FindType("火").find_type()
    df = return_things.drop(["属性", "突破加成"], axis=1)
    list_source = [["produce", "max", "min"]]
    print(df)
    list_source = list_source + [["生命值"] + list(df[df["生命值"] == df["生命值"].max()]["生命值"]) + list(
        df[df["生命值"] == df["生命值"].max()]["生命值"])] + [
                      ["防御力"] + list(df[df["防御力"] == df["防御力"].max()]["防御力"]) + list(
                          df[df["防御力"] == df["防御力"].max()]["防御力"])] + [
                      ["攻击力"] + list(df[df["攻击力"] == df["攻击力"].max()]["攻击力"]) + list(
                          df[df["攻击力"] == df["攻击力"].max()]["攻击力"])]
    c = (
        Bar()
        .add_dataset(
            source=list_source
        )
        .add_yaxis(series_name="max", y_axis=[])
        .add_yaxis(series_name="min", y_axis=[])
        .set_global_opts(
            toolbox_opts=ToolboxOpts(is_show=True),
            title_opts=opts.TitleOpts(title="火属性"),
            xaxis_opts=opts.AxisOpts(type_="category"),
        )
    )
    return c


# 水
def z():
    return_things = FindType("水").find_type()
    df = return_things.drop(["属性", "突破加成"], axis=1)
    list_source = [["produce", "max", "min"]]
    print(df)
    list_source = list_source + [["生命值"] + list(df[df["生命值"] == df["生命值"].max()]["生命值"]) + list(
        df[df["生命值"] == df["生命值"].max()]["生命值"])] + [
                      ["防御力"] + list(df[df["防御力"] == df["防御力"].max()]["防御力"]) + list(
                          df[df["防御力"] == df["防御力"].max()]["防御力"])] + [
                      ["攻击力"] + list(df[df["攻击力"] == df["攻击力"].max()]["攻击力"]) + list(
                          df[df["攻击力"] == df["攻击力"].max()]["攻击力"])]
    c = (
        Bar()
        .add_dataset(
            source=list_source
        )
        .add_yaxis(series_name="max", y_axis=[])
        .add_yaxis(series_name="min", y_axis=[])
        .set_global_opts(
            toolbox_opts=ToolboxOpts(is_show=True),
            title_opts=opts.TitleOpts(title="水属性"),
            xaxis_opts=opts.AxisOpts(type_="category"),
        )
    )
    return c


# 冰
def a():
    return_things = FindType("冰").find_type()
    df = return_things.drop(["属性", "突破加成"], axis=1)
    list_source = [["produce", "max", "min"]]
    print(df)
    list_source = list_source + [["生命值"] + list(df[df["生命值"] == df["生命值"].max()]["生命值"]) + list(
        df[df["生命值"] == df["生命值"].max()]["生命值"])] + [
                      ["防御力"] + list(df[df["防御力"] == df["防御力"].max()]["防御力"]) + list(
                          df[df["防御力"] == df["防御力"].max()]["防御力"])] + [
                      ["攻击力"] + list(df[df["攻击力"] == df["攻击力"].max()]["攻击力"]) + list(
                          df[df["攻击力"] == df["攻击力"].max()]["攻击力"])]
    c = (
        Bar()
        .add_dataset(
            source=list_source
        )
        .add_yaxis(series_name="max", y_axis=[])
        .add_yaxis(series_name="min", y_axis=[])
        .set_global_opts(
            toolbox_opts=ToolboxOpts(is_show=True),
            title_opts=opts.TitleOpts(title="冰属性"),
            xaxis_opts=opts.AxisOpts(type_="category"),
        )
    )
    return c


# 风
def b():
    return_things = FindType("风").find_type()
    df = return_things.drop(["属性", "突破加成"], axis=1)
    list_source = [["produce", "max", "min"]]
    print(df)
    list_source = list_source + [["生命值"] + list(df[df["生命值"] == df["生命值"].max()]["生命值"]) + list(
        df[df["生命值"] == df["生命值"].max()]["生命值"])] + [
                      ["防御力"] + list(df[df["防御力"] == df["防御力"].max()]["防御力"]) + list(
                          df[df["防御力"] == df["防御力"].max()]["防御力"])] + [
                      ["攻击力"] + list(df[df["攻击力"] == df["攻击力"].max()]["攻击力"]) + list(
                          df[df["攻击力"] == df["攻击力"].max()]["攻击力"])]
    c = (
        Bar()
        .add_dataset(
            source=list_source
        )
        .add_yaxis(series_name="max", y_axis=[])
        .add_yaxis(series_name="min", y_axis=[])
        .set_global_opts(
            toolbox_opts=ToolboxOpts(is_show=True),
            title_opts=opts.TitleOpts(title="风属性"),
            xaxis_opts=opts.AxisOpts(type_="category"),
        )
    )
    return c


# 雷
def c():
    return_things = FindType("雷").find_type()
    df = return_things.drop(["属性", "突破加成"], axis=1)
    list_source = [["produce", "max", "min"]]
    print(df)
    list_source = list_source + [["生命值"] + list(df[df["生命值"] == df["生命值"].max()]["生命值"]) + list(
        df[df["生命值"] == df["生命值"].max()]["生命值"])] + [
                      ["防御力"] + list(df[df["防御力"] == df["防御力"].max()]["防御力"]) + list(
                          df[df["防御力"] == df["防御力"].max()]["防御力"])] + [
                      ["攻击力"] + list(df[df["攻击力"] == df["攻击力"].max()]["攻击力"]) + list(
                          df[df["攻击力"] == df["攻击力"].max()]["攻击力"])]
    c = (
        Bar()
        .add_dataset(
            source=list_source
        )
        .add_yaxis(series_name="max", y_axis=[])
        .add_yaxis(series_name="min", y_axis=[])
        .set_global_opts(
            toolbox_opts=ToolboxOpts(is_show=True),
            title_opts=opts.TitleOpts(title="雷属性"),
            xaxis_opts=opts.AxisOpts(type_="category"),
        )
    )
    return c


# 岩
def d():
    return_things = FindType("岩").find_type()
    df = return_things.drop(["属性", "突破加成"], axis=1)
    list_source = [["produce", "max", "min"]]
    print(df)
    list_source = list_source + [["生命值"] + list(df[df["生命值"] == df["生命值"].max()]["生命值"]) + list(
        df[df["生命值"] == df["生命值"].max()]["生命值"])] + [
                      ["防御力"] + list(df[df["防御力"] == df["防御力"].max()]["防御力"]) + list(
                          df[df["防御力"] == df["防御力"].max()]["防御力"])] + [
                      ["攻击力"] + list(df[df["攻击力"] == df["攻击力"].max()]["攻击力"]) + list(
                          df[df["攻击力"] == df["攻击力"].max()]["攻击力"])]
    c = (
        Bar()
        .add_dataset(
            source=list_source
        )
        .add_yaxis(series_name="max", y_axis=[])
        .add_yaxis(series_name="min", y_axis=[])
        .set_global_opts(
            toolbox_opts=ToolboxOpts(is_show=True),
            title_opts=opts.TitleOpts(title="岩属性"),
            xaxis_opts=opts.AxisOpts(type_="category"),
        )
    )
    return c


def e():
    role_things = pd.read_excel("C:/Users/YHT/Desktop/项目/原神各属性角色信息.xlsx", header=0, index_col=0)
    role_things = role_things.fillna(axis=0, method="ffill")
    print(role_things)
    return_things = FindType("岩").find_type()
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
            toolbox_opts=ToolboxOpts(is_show=True),
            title_opts=opts.TitleOpts(title="岩属性"),
            visualmap_opts=opts.VisualMapOpts(type_="size", max_=150, min_=20),
            xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate": 45})
        )
    )
    return c


def f():
    role_things = pd.read_excel("C:/Users/YHT/Desktop/项目/原神各属性角色信息.xlsx", header=0, index_col=0)
    role_things = role_things.fillna(axis=0, method="ffill")
    print(role_things)
    return_things = FindType("火").find_type()
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
            toolbox_opts=ToolboxOpts(is_show=True),
            title_opts=opts.TitleOpts(title="火属性"),
            visualmap_opts=opts.VisualMapOpts(type_="size", max_=150, min_=20),
            xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate": 45})
        )
    )
    return c


def g():
    role_things = pd.read_excel("C:/Users/YHT/Desktop/项目/原神各属性角色信息.xlsx", header=0, index_col=0)
    role_things = role_things.fillna(axis=0, method="ffill")
    print(role_things)
    return_things = FindType("水").find_type()
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
            toolbox_opts=ToolboxOpts(is_show=True),
            title_opts=opts.TitleOpts(title="水属性"),
            visualmap_opts=opts.VisualMapOpts(type_="size", max_=150, min_=20),
            xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate": 45})
        )
    )
    return c


def h():
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
            toolbox_opts=ToolboxOpts(is_show=True),
            title_opts=opts.TitleOpts(title="冰属性"),
            visualmap_opts=opts.VisualMapOpts(type_="size", max_=150, min_=20),
            xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate": 45})
        )
    )
    return c


def I():
    role_things = pd.read_excel("C:/Users/YHT/Desktop/项目/原神各属性角色信息.xlsx", header=0, index_col=0)
    role_things = role_things.fillna(axis=0, method="ffill")
    print(role_things)
    return_things = FindType("风").find_type()
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
            toolbox_opts=ToolboxOpts(is_show=True),
            title_opts=opts.TitleOpts(title="风属性"),
            visualmap_opts=opts.VisualMapOpts(type_="size", max_=150, min_=20),
            xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate": 45})
        )
    )
    return c


def K():
    role_things = pd.read_excel("C:/Users/YHT/Desktop/项目/原神各属性角色信息.xlsx", header=0, index_col=0)
    role_things = role_things.fillna(axis=0, method="ffill")
    print(role_things)
    return_things = FindType("雷").find_type()
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
            toolbox_opts=ToolboxOpts(is_show=True),
            title_opts=opts.TitleOpts(title="雷属性"),
            visualmap_opts=opts.VisualMapOpts(type_="size", max_=150, min_=20),
            xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate": 45})
        )
    )
    return c


page = Page(layout=Page.DraggablePageLayout)
page.add(a(), b(), c(), d(), x(), y(), z(), e(), f(), g(), h(), I(), K())
# page.render(".html")
# Page.save_resize_html(".html", cfg_file=".json", dest="./templates/.html")