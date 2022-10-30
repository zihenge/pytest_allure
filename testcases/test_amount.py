import pytest
import json
import pytest
import requests
import allure
import os
from common.yaml_util import read_yaml

url = "https://test-funny.51k1k.com"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
# #随机数
# Random = random.sample(range(15200000000, 15299999999), 1)
class Testbian:
    # @allure.feature('test_success')
    # @pytest.fixture(scope='session',autouse=True)
    @pytest.mark.flaky(reruns=5, reruns_delay=2)
    def test_tx(self):
        data = {
            'access_token': read_yaml('access_token')
        }

        r = requests.post(url + '/payment/withdraw/h5/withdrawLeft', data=data, headers=headers)
        if r.status_code == 200:
            print("接口返回" + json.dumps(r.json(), indent=2))
        else:
            print("失败" + json.dumps(r.json(), indent=2))
    #      pytest -vs --html .\log\wenjian1.html .\testcases\test_amount.py

    @pytest.mark.flaky(reruns=0, reruns_delay=0)
    def test_tx1(self):
        data = {
            'access_token': read_yaml('access_token')
        }
        req = requests.post(url + '/payment/withdraw/h5/withdrawLeft', data=data, headers=headers)
        result = req.json()
        print(req.text)
        # assert 'leftMoney' in req.text
        assert  result['code'] == 10200 # and


if __name__ == '__main__':
    pytest.main()
