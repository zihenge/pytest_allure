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
    # ������ȡ�����ļ��е��ֻ��Ż�ȡtoken
    def getUsersToken(self):
        # �����ȡ�û��ֻ����룬ֱ�Ӹĳ��Լ��������ļ�
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
                                verify=False)  # ����ssl��֤
            print(req.text)
            # ��ȡtoken����ֶ�
            tokenValue = req.json()["data"]["list"]["access_token"]
            idValue = req.json()["data"]["list"]["user_id"]
            print("��ȡ������token:" + tokenValue, idValue)
            # �ļ������Լ��ã���������Ŀ�ø�Ŀ¼�½�һ��
            f = open('cav_file.csv', 'a+', encoding='utf-8', newline="")
            csv_write = csv.writer(f)
            csv_write.writerow([userPhone, tokenValue, idValue])
            f.close()
    def readCsvPhoneAndToken(self):
        userTokenByPhone = {} #userTokenByPhone���ֵ����ͱ���,Ҳ����json��ʽ�ı���
        with open('cav_file.csv', 'r') as f:  #��cav_file.csv�ļ�������Ϊf
            reader = csv.reader(f) #�ѳ�����f���ݸ�reader����
            for row in reader: #Ȼ��ѭ��
                # ��csv�ļ��е����ݸ�Ϊjson��ʽ��Ȼ�������
                userTokenByPhone[str(row[0])] = row[1]  #����������ֵȡ�������붨��ı����У�Ȼ�󷵻�
        return userTokenByPhone

if __name__ == "__main__":
    # locust -f ִ���ļ�����  --host= ѹ������  --web-host=���ӻ������ָ��·��
    # os.system("locust -f test.py --host=https://test.funny.51k1k.com:443  --web-host=192.168.9.132")
    t = Test()
    # �����ǽ�������¼��ȡ��¼��Token
    t.getUsersToken()
    #�����Ƕ������ļ���׷�ӵķ�ʽ����һֱ�ۼƵģ������Լ�ɾ��CSV�ļ�
    userTokenByPhone = t.readCsvPhoneAndToken()
    keys = userTokenByPhone.keys()
    for key in keys:
        print(key+" "+ userTokenByPhone[key])
