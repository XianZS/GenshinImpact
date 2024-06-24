from pyecharts.charts import Radar
from pyecharts import options as opts
import pandas as pd
from pyecharts.charts import Geo, Map, Bar, Line, Page, Pie, Boxplot, WordCloud
from pyecharts import options as opts
from pyecharts.charts import Scatter
from pyecharts.faker import Faker

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
            legend_opts=opts.LegendOpts(selected_mode="single"),
            title_opts=opts.TitleOpts(title="角色分析(max/min)"),
        )
    )
    return a


def b():
    b = (
        Bar()
        .add_xaxis(["生命值", "防御力", "攻击力"])
        .add_yaxis("max",
                   [int(role_things["生命值"].max()), int(role_things["防御力"].max()),
                    int(role_things["攻击力"].max())])
        .add_yaxis("min",
                   [int(role_things["生命值"].min()), int(role_things["防御力"].min()),
                    int(role_things["攻击力"].min())])
        .set_global_opts(title_opts=opts.TitleOpts(title="分析", subtitle="生命值/防御力/攻击值"))
    )
    return b


def c():
    c = (
        Bar()
        .add_xaxis(list(role_things["角色"][role_things["生命值"] == role_things["生命值"].max()]) +
                   list(role_things["角色"][role_things["防御力"] == role_things["防御力"].max()]) +
                   list(role_things["角色"][role_things["攻击力"] == role_things["攻击力"].max()])
                   )
        .add_yaxis("max",
                   [int(role_things["生命值"].max()), int(role_things["防御力"].max()),
                    int(role_things["攻击力"].max())])
        .set_global_opts(title_opts=opts.TitleOpts(title="柱状图-max", subtitle=""))
    )
    return c


def d():
    d = (
        Bar()
        .add_xaxis(list(role_things["角色"][role_things["生命值"] == role_things["生命值"].min()]) +
                   list(role_things["角色"][role_things["防御力"] == role_things["防御力"].min()]) +
                   list(role_things["角色"][role_things["攻击力"] == role_things["攻击力"].min()])
                   )
        .add_yaxis("min",
                   [int(role_things["生命值"].min()), int(role_things["防御力"].min()),
                    int(role_things["防御力"].min()),
                    int(role_things["攻击力"].min())])
        .set_global_opts(title_opts=opts.TitleOpts(title="柱状图-min", subtitle=""))
    )
    return d


def e():
    e = (
        Scatter()
        .add_xaxis(["生命值-胡桃/菲谢尔", "防御力-七七/(丽莎/凝光)", "攻击力-魈/胡桃"])
        .add_yaxis("max",
                   [int(role_things["生命值"].max()), int(role_things["防御力"].max()),
                    int(role_things["攻击力"].max())])
        .add_yaxis("min",
                   [int(role_things["生命值"].min()), int(role_things["防御力"].min()),
                    int(role_things["攻击力"].min())])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="max&min"),
            visualmap_opts=opts.VisualMapOpts(type_="size", max_=150, min_=20),
        )
    )
    return e


page = Page(layout=Page.DraggablePageLayout)
page.add(a(), b(), c(), d(), e())
# page.render(".html")
# Page.save_resize_html(".html", cfg_file=".json",dest="./tmplates/各数值max&min.html")
