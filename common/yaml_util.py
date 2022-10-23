"""
    公共方法
"""

import os
import yaml

# 读取yaml文件
# 不用run方法执行路径需要是../格式
def read_yaml(key):
    # 用utf-8的形式打开yaml文件，赋值给f
    with open( './caseparams/extract.yml', encoding='utf-8') as f:
        # 加载f文件的内容
        value = yaml.load(stream=f,Loader=yaml.FullLoader)
        # 返回
        return value[key]


# 写入yaml文件，mode='a'用追加的方式去写
def write_yaml(data):
    with open( './caseparams/extract.yml', encoding='utf-8',mode='a') as f:
        yaml.dump(data,stream=f, allow_unicode=True)

# 清空yaml文件,mode='w'写入
def clear_yaml():
    with open('./caseparams/extract.yml', encoding='utf-8',mode='w') as f:
        f.truncate()


# 读取yaml测试用例
    # 用utf-8的形式打开yaml文件，赋值给f
def read_testcase_yaml(yaml_name):
    with open('./caseparams/' + yaml_name, encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
    # 返回
    return value