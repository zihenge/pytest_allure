import json

import requests



class AllRequest:

    session = requests.session()  # 会话

    def all_send_request(self,method,url,data,**kwargs):
        print('------')
        # parans,data,json,files
        # lower()方法转换字符串中所有大写字符为小写
        method = str(method).lower()
        res = None
        if method == 'get':
            res = AllRequest.session.request(method=method,url=url,params=data,**kwargs)
        elif method == 'post':
            # 不管传值是不是健值的字典，都转化个成String
            # strdata = json.dumps(data)
            res = AllRequest.session.request(method=method,url=url,data=data,**kwargs)
        else:
            print('不支持的请求方式')
        return res