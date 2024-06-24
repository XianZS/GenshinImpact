import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Polar, Radar, Page
from pyecharts.charts import Line
from pyecharts.faker import Faker
from pyecharts.faker import Faker
from pyecharts.options import ToolboxOpts
from pyecharts import options as opts
from pyecharts.charts import EffectScatter, Polar
from pyecharts.faker import Faker
from pyecharts.globals import SymbolType
# 各个元素角色信息
from find_type import FindType
from pyecharts.charts import Bar3D

role_things = pd.read_excel("C:/Users/YHT/Desktop/项目/原神各属性角色信息.xlsx", header=0, index_col=0)
role_things = role_things.fillna(axis=0, method="ffill")
print(role_things)
v1 = [[int(role_things["生命值"].max()), int(role_things["防御力"].max()), int(role_things["攻击力"].max())]]
v2 = [[int(role_things["生命值"].min()), int(role_things["防御力"].min()), int(role_things["攻击力"].min())]]
print(v1)


def a():
    a = (
        Radar()
        .add_schema(
            schema=[
                opts.RadarIndicatorItem(name="生命值", max_=17000),
                opts.RadarIndicatorItem(name="攻击力", max_=1000),
                opts.RadarIndicatorItem(name="防御力", max_=500),
            ]
        )
        .add("max", v1)
        .add("min", v2)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            toolbox_opts=ToolboxOpts(is_show=True),
            legend_opts=opts.LegendOpts(selected_mode="single"),
            title_opts=opts.TitleOpts(title="角色分析(max/min)"),
        )
    )
    return a


huo_things = FindType("火").find_type()
shui_things = FindType("水").find_type()
bing_things = FindType("冰").find_type()
feng_things = FindType("风").find_type()
yan_things = FindType("岩").find_type()
lei_things = FindType("雷").find_type()
a1 = [None, int(huo_things["生命值"].max()), int(huo_things["生命值"].min()),
      int(shui_things["生命值"].max()), int(shui_things["生命值"].min()),
      int(bing_things["生命值"].max()), int(bing_things["生命值"].min()),
      int(feng_things["生命值"].max()), int(feng_things["生命值"].min()),
      int(yan_things["生命值"].max()), int(yan_things["生命值"].min()),
      int(lei_things["生命值"].max()), int(lei_things["生命值"].min())]
a4 = [int(huo_things["生命值"].max()), int(huo_things["生命值"].min()),
      int(shui_things["生命值"].max()), int(shui_things["生命值"].min()),
      int(bing_things["生命值"].max()), int(bing_things["生命值"].min()),
      int(feng_things["生命值"].max()), int(feng_things["生命值"].min()),
      int(yan_things["生命值"].max()), int(yan_things["生命值"].min()),
      int(lei_things["生命值"].max()), int(lei_things["生命值"].min())]
print(a1)
a2 = [None, int(huo_things["防御力"].max()), int(huo_things["防御力"].min()),
      int(shui_things["防御力"].max()), int(shui_things["防御力"].min()),
      int(bing_things["防御力"].max()), int(bing_things["防御力"].min()),
      int(feng_things["防御力"].max()), int(feng_things["防御力"].min()),
      int(yan_things["防御力"].max()), int(yan_things["防御力"].min()),
      int(lei_things["防御力"].max()), int(lei_things["防御力"].min())]
a5 = [int(huo_things["防御力"].max()), int(huo_things["防御力"].min()),
      int(shui_things["防御力"].max()), int(shui_things["防御力"].min()),
      int(bing_things["防御力"].max()), int(bing_things["防御力"].min()),
      int(feng_things["防御力"].max()), int(feng_things["防御力"].min()),
      int(yan_things["防御力"].max()), int(yan_things["防御力"].min()),
      int(lei_things["防御力"].max()), int(lei_things["防御力"].min())]
print(a2)
a3 = [None, int(huo_things["攻击力"].max()), int(huo_things["攻击力"].min()),
      int(shui_things["攻击力"].max()), int(shui_things["攻击力"].min()),
      int(bing_things["攻击力"].max()), int(bing_things["攻击力"].min()),
      int(feng_things["攻击力"].max()), int(feng_things["攻击力"].min()),
      int(yan_things["攻击力"].max()), int(yan_things["攻击力"].min()),
      int(lei_things["攻击力"].max()), int(lei_things["攻击力"].min())]
a6 = [int(huo_things["攻击力"].max()), int(huo_things["攻击力"].min()),
      int(shui_things["攻击力"].max()), int(shui_things["攻击力"].min()),
      int(bing_things["攻击力"].max()), int(bing_things["攻击力"].min()),
      int(feng_things["攻击力"].max()), int(feng_things["攻击力"].min()),
      int(yan_things["攻击力"].max()), int(yan_things["攻击力"].min()),
      int(lei_things["攻击力"].max()), int(lei_things["攻击力"].min())]
print(a3)


def b():
    c = (
        Polar()
        .add_schema(
            radiusaxis_opts=opts.RadiusAxisOpts(
                data=["", "火max", "火min", "水max", "水min", "冰max", "冰min", "风max", "风min", "岩max", "岩min",
                      "雷max",
                      "雷min"], type_="category"),
            angleaxis_opts=opts.AngleAxisOpts(is_clockwise=True, max_=17000),
        )
        .add("生命值", a1, type_="bar")
        .set_global_opts(toolbox_opts=ToolboxOpts(is_show=True),
                         title_opts=opts.TitleOpts(title="各属性生命值(max&min)"))
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    )
    return c


def c():
    c = (
        Polar()
        .add_schema(
            radiusaxis_opts=opts.RadiusAxisOpts(
                data=["", "火max", "火min", "水max", "水min", "冰max", "冰min", "风max", "风min", "岩max", "岩min",
                      "雷max",
                      "雷min"], type_="category"),
            angleaxis_opts=opts.AngleAxisOpts(is_clockwise=True, max_=1000),
        )
        .add("防御力", a2, type_="bar")
        .set_global_opts(toolbox_opts=ToolboxOpts(is_show=True),
                         title_opts=opts.TitleOpts(title="各属性防御力(max&min)"))
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    )
    return c


def d():
    c = (
        Polar()
        .add_schema(angleaxis_opts=opts.AngleAxisOpts(data=["火", "水", "风", "冰", "岩", "雷"], type_="category"))
        .add("max", a3[1:14:2], type_="bar", stack="stack0")
        .add("min", a3[0:13:2], type_="bar", stack="stack0")
        .set_global_opts(toolbox_opts=ToolboxOpts(is_show=True), title_opts=opts.TitleOpts(title="各属性攻击力"))
    )
    return c


def e():
    c = (
        Line()
        .add_xaxis(["火max", "火min", "水max", "水min",
                    "冰max", "冰min", "风max", "风min",
                    "岩max", "岩min", "雷max", "雷min"])
        .add_yaxis("生命值浮动变化", a4, is_connect_nones=True)
        .add_yaxis("平均值",
                   [role_things["生命值"].mean(), role_things["生命值"].mean(), role_things["生命值"].mean(),
                    role_things["生命值"].mean(), role_things["生命值"].mean(), role_things["生命值"].mean(),
                    role_things["生命值"].mean(), role_things["生命值"].mean(), role_things["生命值"].mean(),
                    role_things["生命值"].mean(), role_things["生命值"].mean(), role_things["生命值"].mean()]
                   , is_connect_nones=True)
        .add_yaxis("中位数",
                   [role_things["生命值"].median(), role_things["生命值"].median(), role_things["生命值"].median(),
                    role_things["生命值"].median(), role_things["生命值"].median(), role_things["生命值"].median(),
                    role_things["生命值"].median(), role_things["生命值"].median(), role_things["生命值"].median(),
                    role_things["生命值"].median(), role_things["生命值"].median(), role_things["生命值"].median()]
                   , is_connect_nones=True)
        .set_global_opts(toolbox_opts=ToolboxOpts(is_show=True), title_opts=opts.TitleOpts(title="生命值"))
    )
    return c


def f():
    c = (
        Line()
        .add_xaxis(["火max", "火min", "水max", "水min",
                    "冰max", "冰min", "风max", "风min",
                    "岩max", "岩min", "雷max", "雷min"])
        .add_yaxis("防御力浮动变化", a5, is_connect_nones=True)
        .add_yaxis("平均值",
                   [role_things["防御力"].mean(), role_things["防御力"].mean(), role_things["防御力"].mean(),
                    role_things["防御力"].mean(), role_things["防御力"].mean(), role_things["防御力"].mean(),
                    role_things["防御力"].mean(), role_things["防御力"].mean(), role_things["防御力"].mean(),
                    role_things["防御力"].mean(), role_things["防御力"].mean(), role_things["防御力"].mean()]
                   , is_connect_nones=True)
        .add_yaxis("中位数",
                   [role_things["防御力"].median(), role_things["防御力"].median(), role_things["防御力"].median(),
                    role_things["防御力"].median(), role_things["防御力"].median(), role_things["防御力"].median(),
                    role_things["防御力"].median(), role_things["防御力"].median(), role_things["防御力"].median(),
                    role_things["防御力"].median(), role_things["防御力"].median(), role_things["防御力"].median()]
                   , is_connect_nones=True)
        .set_global_opts(toolbox_opts=ToolboxOpts(is_show=True), title_opts=opts.TitleOpts(title="防御力"))
    )
    return c


def g():
    c = (
        Line()
        .add_xaxis(["火max", "火min", "水max", "水min",
                    "冰max", "冰min", "风max", "风min",
                    "岩max", "岩min", "雷max", "雷min"])
        .add_yaxis("攻击力浮动变化", a6, is_connect_nones=True)
        .add_yaxis("平均值",
                   [role_things["攻击力"].mean(), role_things["攻击力"].mean(), role_things["攻击力"].mean(),
                    role_things["攻击力"].mean(), role_things["攻击力"].mean(), role_things["攻击力"].mean(),
                    role_things["攻击力"].mean(), role_things["攻击力"].mean(), role_things["攻击力"].mean(),
                    role_things["攻击力"].mean(), role_things["攻击力"].mean(), role_things["攻击力"].mean()]
                   , is_connect_nones=True)
        .add_yaxis("中位数",
                   [role_things["攻击力"].median(), role_things["攻击力"].median(), role_things["攻击力"].median(),
                    role_things["攻击力"].median(), role_things["攻击力"].median(), role_things["攻击力"].median(),
                    role_things["攻击力"].median(), role_things["攻击力"].median(), role_things["攻击力"].median(),
                    role_things["攻击力"].median(), role_things["攻击力"].median(), role_things["攻击力"].median()]
                   , is_connect_nones=True)
        .set_global_opts(toolbox_opts=ToolboxOpts(is_show=True), title_opts=opts.TitleOpts(title="攻击力"))
    )
    return c


def h():
    # x轴:
    hours = ["火属性", "火属性", "火属性", "火属性", "火属性", "火属性", "火属性", "火属性", "火属性",
             "水属性", "水属性", "水属性", "水属性", "水属性", "水属性", "水属性", "水属性", "水属性",
             "冰属性", "冰属性", "冰属性", "冰属性", "冰属性", "冰属性", "冰属性", "冰属性", "冰属性",
             "风属性", "风属性", "风属性", "风属性", "风属性", "风属性", "风属性", "风属性", "风属性",
             "雷属性", "雷属性", "雷属性", "雷属性", "雷属性", "雷属性", "雷属性", "雷属性", "雷属性",
             "岩属性", "岩属性", "岩属性", "岩属性", "岩属性", "岩属性", "岩属性", "岩属性", "岩属性", ]
    # y轴:[0,1,2]
    days = ["生命值(/10)", "防御力", "攻击力"]

    data = [
        [0, 0, int(huo_things["生命值"][0]) / 10],
        [0, 1, int(huo_things["生命值"][1]) / 10],
        [0, 2, int(huo_things["生命值"][2]) / 10],
        [0, 3, int(huo_things["生命值"][3]) / 10],
        [0, 4, int(huo_things["生命值"][4]) / 10],
        [0, 5, int(huo_things["生命值"][5]) / 10],
        [0, 6, int(huo_things["生命值"][6]) / 10],
        [0, 7, int(huo_things["生命值"][7]) / 10],
        [0, 8, int(huo_things["生命值"][8]) / 10],
        [0, 9, int(shui_things["生命值"][0]) / 10],
        [0, 10, int(shui_things["生命值"][1]) / 10],
        [0, 11, int(shui_things["生命值"][2]) / 10],
        [0, 12, int(shui_things["生命值"][3]) / 10],
        [0, 13, int(shui_things["生命值"][4]) / 10],
        [0, 14, 0],
        [0, 15, 0],
        [0, 16, 0],
        [0, 17, 0],
        [0, 18, int(bing_things["生命值"][0]) / 10],
        [0, 19, int(bing_things["生命值"][1]) / 10],
        [0, 20, int(bing_things["生命值"][2]) / 10],
        [0, 21, int(bing_things["生命值"][3]) / 10],
        [0, 22, int(bing_things["生命值"][4]) / 10],
        [0, 23, int(bing_things["生命值"][5]) / 10],
        [0, 24, int(bing_things["生命值"][6]) / 10],
        [0, 25, int(bing_things["生命值"][7]) / 10],
        [0, 26, int(bing_things["生命值"][8]) / 10],
        [0, 27, int(feng_things["生命值"][0]) / 10],
        [0, 28, int(feng_things["生命值"][1]) / 10],
        [0, 29, int(feng_things["生命值"][2]) / 10],
        [0, 30, int(feng_things["生命值"][3]) / 10],
        [0, 31, int(feng_things["生命值"][4]) / 10],
        [0, 32, int(feng_things["生命值"][5]) / 10],
        [0, 33, 0],
        [0, 34, 0],
        [0, 35, 0],
        [0, 36, int(lei_things["生命值"][0]) / 10],
        [0, 37, int(lei_things["生命值"][1]) / 10],
        [0, 38, int(lei_things["生命值"][2]) / 10],
        [0, 39, int(lei_things["生命值"][3]) / 10],
        [0, 40, int(lei_things["生命值"][4]) / 10],
        [0, 41, int(lei_things["生命值"][5]) / 10],
        [0, 42, int(lei_things["生命值"][6]) / 10],
        [0, 43, 0],
        [0, 44, 0],
        [0, 45, int(yan_things["生命值"][0]) / 10],
        [0, 46, int(yan_things["生命值"][1]) / 10],
        [0, 47, int(yan_things["生命值"][2]) / 10],
        [0, 48, int(yan_things["生命值"][3]) / 10],
        [0, 49, 0],
        [0, 50, 0],
        [0, 51, 0],
        [0, 52, 0],
        [0, 53, 0],
        [1, 0, int(huo_things["防御力"][0])],
        [1, 1, int(huo_things["防御力"][1])],
        [1, 2, int(huo_things["防御力"][2])],
        [1, 3, int(huo_things["防御力"][3])],
        [1, 4, int(huo_things["防御力"][4])],
        [1, 5, int(huo_things["防御力"][5])],
        [1, 6, int(huo_things["防御力"][6])],
        [1, 7, int(huo_things["防御力"][7])],
        [1, 8, int(huo_things["防御力"][8])],
        [1, 9, int(shui_things["防御力"][0])],
        [1, 10, int(shui_things["防御力"][1])],
        [1, 11, int(shui_things["防御力"][2])],
        [1, 12, int(shui_things["防御力"][3])],
        [1, 13, int(shui_things["防御力"][4])],
        [1, 14, 0],
        [1, 15, 0],
        [1, 16, 0],
        [1, 17, 0],
        [1, 18, int(bing_things["防御力"][0])],
        [1, 19, int(bing_things["防御力"][1])],
        [1, 20, int(bing_things["防御力"][2])],
        [1, 21, int(bing_things["防御力"][3])],
        [1, 22, int(bing_things["防御力"][4])],
        [1, 23, int(bing_things["防御力"][5])],
        [1, 24, int(bing_things["防御力"][6])],
        [1, 25, int(bing_things["防御力"][7])],
        [1, 26, int(bing_things["防御力"][8])],
        [1, 27, int(feng_things["防御力"][0])],
        [1, 28, int(feng_things["防御力"][1])],
        [1, 29, int(feng_things["防御力"][2])],
        [1, 30, int(feng_things["防御力"][3])],
        [1, 31, int(feng_things["防御力"][4])],
        [1, 32, int(feng_things["防御力"][5])],
        [1, 33, 0],
        [1, 34, 0],
        [1, 35, 0],
        [1, 36, int(lei_things["防御力"][0])],
        [1, 37, int(lei_things["防御力"][1])],
        [1, 38, int(lei_things["防御力"][2])],
        [1, 39, int(lei_things["防御力"][3])],
        [1, 40, int(lei_things["防御力"][4])],
        [1, 41, int(lei_things["防御力"][5])],
        [1, 42, int(lei_things["防御力"][6])],
        [1, 43, 0],
        [1, 44, 0],
        [1, 45, int(yan_things["防御力"][0])],
        [1, 46, int(yan_things["防御力"][1])],
        [1, 47, int(yan_things["防御力"][2])],
        [1, 48, int(yan_things["防御力"][3])],
        [1, 49, 0],
        [1, 50, 0],
        [1, 51, 0],
        [1, 52, 0],
        [1, 53, 0],
        [2, 0, int(huo_things["攻击力"][0])],
        [2, 1, int(huo_things["攻击力"][1])],
        [2, 2, int(huo_things["攻击力"][2])],
        [2, 3, int(huo_things["攻击力"][3])],
        [2, 4, int(huo_things["攻击力"][4])],
        [2, 5, int(huo_things["攻击力"][5])],
        [2, 6, int(huo_things["攻击力"][6])],
        [2, 7, int(huo_things["攻击力"][7])],
        [2, 8, int(huo_things["攻击力"][8])],
        [2, 9, int(shui_things["攻击力"][0])],
        [2, 10, int(shui_things["攻击力"][1])],
        [2, 11, int(shui_things["攻击力"][2])],
        [2, 12, int(shui_things["攻击力"][3])],
        [2, 13, int(shui_things["攻击力"][4])],
        [2, 14, 0],
        [2, 15, 0],
        [2, 16, 0],
        [2, 17, 0],
        [2, 18, int(bing_things["攻击力"][0])],
        [2, 19, int(bing_things["攻击力"][1])],
        [2, 20, int(bing_things["攻击力"][2])],
        [2, 21, int(bing_things["攻击力"][3])],
        [2, 22, int(bing_things["攻击力"][4])],
        [2, 23, int(bing_things["攻击力"][5])],
        [2, 24, int(bing_things["攻击力"][6])],
        [2, 25, int(bing_things["攻击力"][7])],
        [2, 26, int(bing_things["攻击力"][8])],
        [2, 27, int(feng_things["攻击力"][0])],
        [2, 28, int(feng_things["攻击力"][1])],
        [2, 29, int(feng_things["攻击力"][2])],
        [2, 30, int(feng_things["攻击力"][3])],
        [2, 31, int(feng_things["攻击力"][4])],
        [2, 32, int(feng_things["攻击力"][5])],
        [2, 33, 0],
        [2, 34, 0],
        [2, 35, 0],
        [2, 36, int(lei_things["攻击力"][0])],
        [2, 37, int(lei_things["攻击力"][1])],
        [2, 38, int(lei_things["攻击力"][2])],
        [2, 39, int(lei_things["攻击力"][3])],
        [2, 40, int(lei_things["攻击力"][4])],
        [2, 41, int(lei_things["攻击力"][5])],
        [2, 42, int(lei_things["攻击力"][6])],
        [2, 43, 0],
        [2, 44, 0],
        [2, 45, int(yan_things["攻击力"][0])],
        [2, 46, int(yan_things["攻击力"][1])],
        [2, 47, int(yan_things["攻击力"][2])],
        [2, 48, int(yan_things["攻击力"][3])],
        [2, 49, 0],
        [2, 50, 0],
        [2, 51, 0],
        [2, 52, 0],
        [2, 53, 0],
    ]
    data = [[d[1], d[0], d[2]] for d in data]

    c = (
        Bar3D()
        .add(
            series_name="分析",
            data=data,
            xaxis3d_opts=opts.Axis3DOpts(type_="category", data=hours),
            yaxis3d_opts=opts.Axis3DOpts(type_="category", data=days),
            zaxis3d_opts=opts.Axis3DOpts(type_="value"),
        )
        .set_global_opts(
            toolbox_opts=ToolboxOpts(is_show=True),
            visualmap_opts=opts.VisualMapOpts(
                max_=1700,
                range_color=[
                    "#313695",
                    "#4575b4",
                    "#74add1",
                    "#abd9e9",
                    "#e0f3f8",
                    "#ffffbf",
                    "#fee090",
                    "#fdae61",
                    "#f46d43",
                    "#d73027",
                    "#a50026",
                ],
            )
        )
    )
    return c


def i():
    c = (
        EffectScatter()
        .add_xaxis(["生命力(/10)", "防御力", "攻击力"])
        .add_yaxis("std标准差",
                   [int(role_things["生命值"].std()) / 10,
                    int(role_things["防御力"].std()),
                    int(role_things["攻击力"].std())],
                   symbol=SymbolType.ARROW)
        .set_global_opts(toolbox_opts=ToolboxOpts(is_show=True), title_opts=opts.TitleOpts(title="标准差"))
    )
    return c


page = Page(layout=Page.DraggablePageLayout)
page.add(a(), b(), c(), d(), e(), f(), g(), h(), i())
# page.render(".html")
# Page.save_resize_html(".html", cfg_file=".json", dest="./templates/.html")