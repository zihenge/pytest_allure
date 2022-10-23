# import os
#
# import allure
# import pytest
# import json
# import requests
# import time
# import csv
# import random
# import urllib.parse
#
# url = "https://test-funny.51k1k.com"
# headers = {"Content-Type": "application/x-www-form-urlencoded"}
# class Test_jk1:
#     def test_login(self):
#         data = {'MY_APP_VERSION': '1.1.0',
#                 'access_token': '',
#                 'api_name': "kyk.userV217.signin",
#                 'appid': '1',
#                 'apple_user_id': '',
#                 'channel_id': '20001',
#                 'client_type': '0',
#                 'device_unique_id': '00000000-0000-0000-0000-000000000000',
#                 'from_new_user_boss': '0',
#                 'mobile': '18671490914',
#                 'os': 'ios',
#                 'sign': 'a6edc1128a7b855ff633c2830d2a932e',
#                 'simulator_check': '0',
#                 'time': '1665993951',
#                 'token': 'eb86fa064482989312e2a1557ddb4032',
#                 'utid': 'Yq/rb15Hi8UDAPUGRpo/FFtJ',
#                 'verify_code': 111111,
#                 'version': '1.1.0',
#                 }
#         r = requests.post(url + "/api/api/", data=data, headers=headers)
#         if r.status_code == 200:
#             print("接口返回" + json.dumps(r.json(), indent=2))
#         else:
#             print("失败" + json.dumps(r.json(), indent=2))
#         # 提取token
#         token_value = r.json()["data"]["list"]["access_token"]
#         print(token_value)
#         return token_value
#         # token = tokenValue
#         # return token;