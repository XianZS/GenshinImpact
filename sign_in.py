"""判断用户输入的登录信息是否正确"""
from flask import render_template
from pandas import DataFrame, Series
import pandas as pd
import numpy as np


class SignIn:
    def __init__(self, request_x, request_y):
        self.request_x = request_x
        self.request_y = request_y

    def sign_in(self):
        # 读取excel表格(用户信息)
        user_things = pd.read_excel("C:/Users/YHT/Desktop/项目/用户信息.xlsx")
        # 得到存储账号的Series表格
        user_account0 = user_things["账号"]
        user_password0 = user_things["密码"]
        # 得到用户输入的账号和密码<class 'str'>
        user_account1 = self.request_x
        print(user_account1,type(user_account1))
        user_password1 = self.request_y
        # 判断用户输入信息的正确性
        for account in user_account0:
            # 此处account类型<class 'float'>
            if str(int(account)) == user_account1:
                for password in user_password0:
                    if str(int(password)) == user_password1:
                        return render_template("主页面.html")
                    else:
                        return "密码错误"
            else:
                return "用户不存在"
