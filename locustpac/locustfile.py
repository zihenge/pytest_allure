from locust import HttpUser,task
import queue
import loader
import os
import json
import time
import calendar
import yaml
# 不重复读取CSV的数据
q = queue.Queue()
csv_list = loader.losd_csv_file( r"C:\Users\dyd9981\PycharmProjects\pythonProject8\data\User.csv")
for item in csv_list:
    q.put(item)

class FecMallUser(HttpUser):
    min_wait = 1000
    max_wait = 3000

    @task(1)
    def login(self):
        item = q.get()
        # 获取当前时间戳
        timeStamp = calendar.timegm(time.gmtime())
        data = {"MY_APP_VERSION": "1.1.0",
                                      "access_token": "",
                                      "api_name": "kyk.userV217.signin",
                                      "ts":timeStamp,
                                      "appid": "1",
                                      "apple_user_id": "",
                                      "channel_id": "20001",
                                      "client_type": "0",
                                      "device_unique_id": "00000000-0000-0000-0000-000000000000",
                                      "from_new_user_boss": "0",
                                      "mobile": item.get("mobile"),
                                      "os": "ios",
                                      "sign": "da1adf06d5909cec2378e15a84565d48",
                                      "simulator_check": "0",
                                      "time": time,
                                      "token": "eb86fa064482989312e2a1557ddb4032",
                                      "utid": "YWEOXTm5zboDAKiW1VYbkOdY",
                                      "verify_code": item.get("verify_code"),
                                      "version": "1.1.0",
                                      }

        # data = {"email" : item.get("email"),"password" : item.get("password")}
        response = self.client.post(url="/api/api/",data=data)
        d = response.json()
        if response.status_code == 200:
            print("success")
        else:
            print("fails")
        print("接口返回" + json.dumps(response.json(), indent=2))

        # 把token值写入配置文件中
        yamlpath = r"C:\Users\dyd9981\PycharmProjects\pythonProject8\locustpac\token.csv"
        # 提取token字段
        tokenValue = {
            'access_token': response.json()["data"]["list"]["access_token"]
        }
        with open(yamlpath, "w", encoding='UTF-8') as f:
            yaml.dump(tokenValue,f,allow_unicode=True)


if __name__ == "__main__":
    # locust -f 执行文件名称  --host= 压测域名  --web-host=可视化界面的指定路由
    os.system("locust -f locustfile.py --host=https://test.funny.51k1k.com:443  --web-host=192.168.40.195")