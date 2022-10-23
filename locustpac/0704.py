# coding=gbk
from locust import HttpUser, task, HttpLocust, between
import os
import json
import random
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from utils.ReadFileUtils import ReadFileUtils
import configparser
config = configparser.ConfigParser()
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class TaskLocust(HttpUser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.userIds = ReadFileUtils().readCsvFile(r'C:\Users\dyd9981\PycharmProjects\pythonProject8\sources\userIdsList')
    @task(1)
    def CFG(self):
            # req = self.client.get("请求地址", headers=,data, verify=False)   返回的req为接口返回的相关信息
            req = self.client.get("/boss/system/check/mongoUserMatch?1=1", headers={}, verify=False)
            if req.status_code == 200:
                print("success")
            else:
                print("fails")
            print("接口返回" + json.dumps(req.json(), indent=2));

            req = self.client.get("/boss/system/check/userInfoByIdForMysql?userId=109856", headers={}, verify=False)
            if req.status_code == 200:
                print("success")
            else:
                print("fails")
            print("接口返回" + json.dumps(req.json(), indent=2));
            # post 请求
            # req = self.client.post("/api/api/",data={"MY_APP_VERSION": "1.1.0", },verify=False)# 避免ssl认证
            # if req.status_code == 200:
            #     print("success")
            # else:
            #     print("fails")
    # @task(1)
    # def MYsql(self):
    #         req = self.client.get("/boss/system/check/userInfoByIdForMysql?userId=109856", headers={}, verify=False)
    #         if req.status_code == 200:
    #             print("success")
    #         else:
    #             print("fails")
    #         print("接口返回" + json.dumps(req.json(), indent=2));

    # @task(1)
    # def Redis(self):
    #         req = self.client.get("/boss/system/check/userInfoByIdForRedis?userId=109856", headers={}, verify=False)
    #         if req.status_code == 200:
    #             print("success")
    #         else:
    #             print("fails")
    #         print("接口返回" + json.dumps(req.json(), indent=2));
    #
    # @task(5)
    # def RedisToMap(self):
    #         req = self.client.get("/boss/system/check/userInfoByIdForRedisToMap?userId=109856", headers={}, verify=False)
    #         if req.status_code == 200:
    #             print("success")
    #         else:
    #             print("fails")
    #         print("接口返回" + json.dumps(req.json(), indent=2));

if __name__ == "__main__":
    # locust -f 执行文件名称  --host= 压测域名  --web-host=可视化界面的指定路由
    min_wait = 2000
    max_wait = 3000
    os.system("locust -f 0704.py --host=https://test-middle.51k1k.com:443  --web-host=192.168.40.195")   # 测试
