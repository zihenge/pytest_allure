from locust import HttpUser,task
import queue
import loader
import os

q = queue.Queue()
# 会重复读取csv数据
class FecMallUser(HttpUser):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.q = queue.Queue()

    def on_start(self):
        csv_list = loader.losd_csv_file( r"C:\Users\dyd9981\PycharmProjects\pythonProject8\data\User.csv")
        for item in csv_list:
            self.q.put(item)


    @task
    def login(self):
        item = q.get()
        data = {"email" : item.get("email"),"password" : item.get("password")}
        response = self.client.post(url="/api/api/",data=data)
        d = response.json()
        self.q.put(item)

# if __name__ == "__main__":
#     # locust -f 执行文件名称  --host= 压测域名  --web-host=可视化界面的指定路由
#     os.system("locust -f Repeatread.py --host=https://test.funny.51k1k.com:443  --web-host=192.168.9.132")