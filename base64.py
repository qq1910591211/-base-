#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/17 15:58
# @Author  : shanfenglan
# @File    : ftob64.py
# @Software: PyCharm
import base64, sys, time

# 确保用户提供了文件路径
if len(sys.argv) < 2:
    print("用法: python ftob64.py <文件路径>")
    sys.exit(1)

# 获取用户指定的文件路径
path = sys.argv[1]

try:
    with open(path, 'rb') as file:  # 以二进制方式打开文件
        data = file.read()  # 读取文件内容
        encoded_str = base64.b64encode(data)  # 对数据进行base64编码

    # 打印编码后的字符串
    print(encoded_str.decode())  # decode()将bytes类型转为str类型，以便正确显示

except IOError as e:
    print("无法打开文件：", e)
except Exception as e:
    print("发生错误：", e)