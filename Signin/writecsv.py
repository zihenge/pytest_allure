# coding=gbk
from locust import HttpUser, task, HttpLocust, between
import os
import json
import csv
import random
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import configparser
import time

from utils.ReadFileUtils import ReadFileUtils

config = configparser.ConfigParser()
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
class Test():
    # 批量读取配置文件中得手机号获取token
    def getUsersToken(self):
        # 这里读取用户手机号码，直接改成自己得配置文件
        self.userIds = ReadFileUtils().readCsvFile(r'C:\Users\dyd9981\PycharmProjects\pythonProject8\sources\userIdsList')
        # userIds = [13821342123, 12112345602, 15899999991, 13312345602, 13312345605, 15845464979, 16798784646,
        #            13312345665, 15555555538, 13000000011]
        userIds = self.userIds
        for userPhone in userIds:
            req = requests.post("https://pre-funny.51k1k.com/api/api/",
                                data={"wifi": "72:ea:b0:01:e5:9e",
                                      "os": "android",
                                      "mobile": userPhone,
                                      "sign": "372b0b6ead372ba559ea85a98f5990c2",
                                      "verify_code": "111111",
                                      "from_new_user_boss": "2",
                                      "client_type": "0",
                                      "utid":"YP9t+d/SjAYDAF1TZJ+ZMGZs",
                                      "version":"1.6.1",
                                      "token":"eb86fa064482989312e2a1557ddb4032",
                                      "access_token":"",
                                      "simulator_check":"0.5",
                                      "user_id":"",
                                      "api_name":"kyk.userV217.signin",
                                      "appid":"1",
                                      "system_os":"8.1.0",
                                      "imei":"27f43c76-f3df-4587-82b6-31dda66bc2dd",
                                      "time":"1664334016",
                                      "device_unique_id":"27f43c76-f3df-4587-82b6-31dda66bc2dd",
                                      "channel_id":"20002"
                                      },
                                verify=False)  # 避免ssl认证
            print(req.text)
            # 提取token相关字段
            tokenValue = req.json()["data"]["list"]["access_token"]
            idValue = req.json()["data"]["list"]["user_id"]
            print("提取出来得token:" + tokenValue, idValue)
            # 文件换成自己得，或者在项目得根目录下建一个
            f = open('cav_file.csv', 'a+', encoding='utf-8', newline="")
            csv_write = csv.writer(f)
            csv_write.writerow([userPhone, tokenValue, idValue])
            f.close()
    def readCsvPhoneAndToken(self):
        userTokenByPhone = {} #userTokenByPhone是字典类型变量,也就是json格式的变量
        with open('cav_file.csv', 'r') as f:  #打开cav_file.csv文件，命名为f
            reader = csv.reader(f) #把出来的f数据给reader变量
            for row in reader: #然后循环
                # 将csv文件中得内容改为json格式，然后读出来
                userTokenByPhone[str(row[0])] = row[1]  #将读出来的值取出来放入定义的变量中，然后返回
        return userTokenByPhone

if __name__ == "__main__":
    # locust -f 执行文件名称  --host= 压测域名  --web-host=可视化界面的指定路由
    # os.system("locust -f test.py --host=https://test.funny.51k1k.com:443  --web-host=192.168.9.132")
    t = Test()
    # 以下是将操作登录获取登录得Token
    t.getUsersToken()
    #以下是读配置文件，追加的方式，会一直累计的，用完自己删除CSV文件
    userTokenByPhone = t.readCsvPhoneAndToken()
    keys = userTokenByPhone.keys()
    for key in keys:
        print(key+" "+ userTokenByPhone[key])
