import re
import time
import pytest
import requests
import json
from common.yaml_util import write_yaml

url = "https://test-funny.51k1k.com"
headers = {"Content-Type": "application/x-www-form-urlencoded"}

class TestApi:
    csrf_tokne = ''
    # session = requests.session()  #回话
    def test_login(self):
        # clear_yaml()
        # yield
        data = {'MY_APP_VERSION': '1.1.0',
                'access_token': '',
                'api_name': "kyk.userV217.signin",
                'appid': '1',
                'apple_user_id': '',
                'channel_id': '20001',
                'client_type': '0',
                'device_unique_id': '00000000-0000-0000-0000-000000000000',
                'from_new_user_boss': '0',
                'mobile': '18671490914',
                'os': 'ios',
                'sign': 'a6edc1128a7b855ff633c2830d2a932e',
                'simulator_check': '0',
                'time': '1665993951',
                'token': 'eb86fa064482989312e2a1557ddb4032',
                'utid': 'Yq/rb15Hi8UDAPUGRpo/FFtJ',
                'verify_code': 111111,
                'version': '1.1.0',
                }
        req = requests.post(url + "/api/api/", data=data, headers=headers)
        result = req.json()
        print(req.text)
        # assert 'leftMoney' in req.text
        assert result['code'] == 0  # and
        #通过write_yaml方法写入yaml文件
        extract_data = {"access_token" : req.json()["data"]["list"]["access_token"]}
        print(extract_data)
        # write_yaml(extract_data)
    # def test_login0(self):
    #         # clear_yaml()
    #         # yield
    #     data = {'MY_APP_VERSION': '1.1.0',
    #                 'access_token': '',
    #                 'api_name': "kyk.userV217.signin",
    #                 'appid': '1',
    #                 'apple_user_id': '',
    #                 'channel_id': '20001',
    #                 'client_type': '0',
    #                 'device_unique_id': '00000000-0000-0000-0000-000000000000',
    #                 'from_new_user_boss': '0',
    #                 'mobile': '110',
    #                 'os': 'ios',
    #                 'sign': 'a6edc1128a7b855ff633c2830d2a932e',
    #                 'simulator_check': '0',
    #                 'time': '1665993951',
    #                 'token': 'eb86fa064482989312e2a1557ddb4032',
    #                 'utid': 'Yq/rb15Hi8UDAPUGRpo/FFtJ',
    #                 'verify_code': 000000,
    #                 'version': '1.1.0',
    #                 }
    #     r = requests.post(url + "/api/api/", data=data, headers=headers)
    #     if r.status_code == 200:
    #         print("接口返回" + json.dumps(r.json(), indent=2))
    #     else:
    #         print("失败" + r.text)
