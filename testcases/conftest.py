# import pytest
#
# from common.yaml_util import clear_yaml
#
# #每个会话之前的操作，执行run文件时，调用清空clear_yaml()方法
# @pytest.fixture(scope='session',autouse=True)
# def execute_database_sql():
#     print("在所有请求前执行一次")
#     clear_yaml()
#     yield
#     print('在所有请求后执行一次')