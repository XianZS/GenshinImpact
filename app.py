from flask import Flask, render_template, request

"""自定义class"""
# 各个元素角色信息
from find_type import FindType
# 登录页面
from sign_in import SignIn
# 设置参数要求，查找对应角色
from NUM import Num
# 按要求排列
from SORT import Sort
# 查找某一角色
from FR import FindRole
# 画图散点图、漏斗图
from WRITEPHOTO import WriteScatter, WriteFunnel, WriteBarData, WritePie, WriteLineBar

app = Flask(__name__)

"""首页"""


# 首页
@app.route("/")
def first_page():
    return render_template("主页面.html")


"""登录"""


# 登录-1，显示登录页面
@app.route("/sign_in")
def sign_in():
    return render_template("登录.html")


# 登录-2，判断用户输入的信息是否正确
@app.route("/input_sign_in")
def input_sign_in():
    x = SignIn(request.args.get("账号"), request.args.get("密码")).sign_in()
    return x


"""注册"""


# 注册-1，显示注册页面
@app.route("/sign_up")
def sign_up():
    return render_template("注册.html")


# 注册-2，接收用户输入的信息
@app.route("/input_sign_up")
def input_sing_up():
    return render_template("注册成功.html")
    # df.to_excel("C:/Users/YHT/Desktop/项目/用户注册信息.xlsx")


# 主页面-登录/注册成功之后的页面-数据页面
@app.route("/home_page")
def home_page():
    return render_template("主页面.html")


"""各属性角色信息"""


# 火属性角色
@app.route("/huo_type")
def huo_type():
    # 得到分组之后结果
    return_things = FindType("火").find_type()
    # 先删除[“属性”,“突破加成”]两列，再将其传入
    WriteBarData(return_things.drop(["属性", "突破加成"], axis=1)).write_bar_data()
    # 展示数据
    return render_template("数据集-自动生成.html")


@app.route("/huo_photo")
def huo_photo():
    return render_template("火属性.html")


# 水属性角色
@app.route("/shui_type")
def shui_type():
    return_things = FindType("水").find_type()
    WriteBarData(return_things.drop(["属性", "突破加成"], axis=1)).write_bar_data()
    return render_template("数据集-自动生成.html")


@app.route("/shui_photo")
def shui_photo():
    return render_template("水属性.html")


# 冰属性角色
@app.route("/bing_type")
def bing_type():
    return_things = FindType("冰").find_type()
    WriteBarData(return_things.drop(["属性", "突破加成"], axis=1)).write_bar_data()
    return render_template("数据集-自动生成.html")


@app.route("/bing_photo")
def bing_photo():
    return render_template("冰属性.html")


# 风属性角色
@app.route("/feng_type")
def feng_type():
    return_things = FindType("风").find_type()
    WriteBarData(return_things.drop(["属性", "突破加成"], axis=1)).write_bar_data()
    return render_template("数据集-自动生成.html")


@app.route("/feng_photo")
def feng_photo():
    return render_template("风属性.html")


# 雷属性角色
@app.route("/lei_type")
def lei_type():
    return_things = FindType("雷").find_type()
    WriteBarData(return_things.drop(["属性", "突破加成"], axis=1)).write_bar_data()
    return render_template("数据集-自动生成.html")


@app.route("/lei_photo")
def lei_photo():
    return render_template("雷属性.html")


# 岩属性角色
@app.route("/yan_type")
def yan_type():
    return_things = FindType("岩").find_type()
    WriteBarData(return_things.drop(["属性", "突破加成"], axis=1)).write_bar_data()
    return render_template("数据集-自动生成.html")


@app.route("/yan_photo")
def yan_photo():
    return render_template("岩属性.html")


"""筛选符合要求的角色：筛选"""


# 传入参数为生命力/防御力/攻击力的限制数值，按照要求筛选出符合的角色
# 比如，要找出生命值高于10000，防御力高于270，攻击力高于300的角色
# sift：筛选
@app.route("/Sift_things")
def Sift_things():
    # 得到筛选之后结果
    df = Num(int(request.args.get("生命值")), int(request.args.get("防御力")), int(request.args.get("攻击力"))).num()
    # 将筛选之后的结果，处理成html文件
    WriteScatter(df["角色"], df["生命值"], df["防御力"], df["攻击力"]).write_scatter()
    return render_template("筛选结果-自动生成.html")


"""按要求排列：排行"""


# 传入参数为生命值/防御力/攻击力，将按照生命值/防御力/攻击力将角色重新排序，默认从小到大
@app.route("/Sort_by")
def Sort_by():
    # 先得到某一属性的全部角色——>DataFrame数组
    return_things = FindType(request.args.get("属性")).find_type()
    # 根据排序条件，对该数组的角色进行排序
    df = Sort(request.args.get("排序条件"), return_things).sort()
    # 传入参数为两个Series数组，将其转换为漏斗图
    WriteFunnel(df["角色"], df[request.args.get("排序条件")]).write_funnel()
    return render_template("排序结果-自动生成.html")


"""查找某一角色：查找"""


# 传入参数为角色名称，查找出该角色一切数值
@app.route("/find_role")
def find_role():
    Series_list = FindRole(request.args.get("查找条件")).findrole()
    WritePie(Series_list[["生命值", "防御力", "攻击力"]], Series_list["属性"], Series_list["突破加成"]).write_pie()
    return render_template("单个角色数据-自动生成.html")


"""显示全部角色"""


@app.route("/all_role")
def All_Role():
    # 作图详细见"ALL[].py"文件
    return render_template("所有角色-自动生成.html")


"""最大最小对比"""


@app.route("/max_and_min")
def MAX_AND_MIN():
    # 作图详细见“max&min[].py”
    return render_template("各数值max&min.html")


"""数据比较展示"""


# 作图详细见”数据对比显示[].py“文件
@app.route("/Compare_things")
def Compare_things():
    return render_template("数据比较展示.html")


"""未来数据预测"""


@app.route("/Culture_num")
def culture_num():

    return "数据预测页面"


if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0",
            port=8000)
