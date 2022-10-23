import pytest
import json
import pytest
import requests
import allure
import os

from common.all_request import AllRequest
from common.yaml_util import read_testcase_yaml, write_yaml

# from testcases.test_Signin import Test_jk1

# url = "https://test-funny.51k1k.com"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
# #随机数
# Random = random.sample(range(15200000000, 15299999999), 1)
class Testtx:
    # 全局变量
    access_token = ""
    # 第一步：发送一个请求，用于设置请求中的cookies
    # 实例化session
    # session = requests.session()   #会话
    @pytest.mark.parametrize("caseinfo",read_testcase_yaml("config.yml"))
    def test_get_token(self,caseinfo):
        # print(caseinfo)
        print(caseinfo['name'])
        # # 获取方法
        # print(caseinfo['request']['url'])
        # print(caseinfo['request']['json'])
        # print(caseinfo['request']['method'])
        # print(caseinfo['validate'])

        url = caseinfo['request']['url']
        data = caseinfo['request']['json']
        method = caseinfo['request']['method']
        validata = caseinfo['validate']
        if method == 'get':
            res = AllRequest().all_send_request(method, url=url, data=data)
            # requests.get()
        else:
            res = AllRequest().all_send_request(method, url=url, data=data)
            # 把返回值给result变量
            result = res.json()

            if "access_token" in json.dumps(result):
                extract_data = Testtx.access_token ={ 'access_token': result["data"]["list"]["access_token"]}
                # print(result)
                # 通过write_yaml方法写入yaml文件
                write_yaml(extract_data)
            print("接口返回" + json.dumps(res.json(), indent=2)) #返回值转成json
            for val in validata:
                # print(val['eq']['code'])
                assert val['eq']['code'] == res.json()['code']




