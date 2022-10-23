import unittest
import pytest
# from gevent import os
import os


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # pytest.main(["-s","allure-test.py"])
        '''
        -q: 安静模式, 不输出环境信息
        -v: 丰富信息模式, 输出更详细的用例执行信息
        -s: 显示程序中的print/logging输出
        '''
        pytest.main(['-s', '-q', 'test_amount.py', '--clean-alluredir', '--alluredir=allure-results'])
        os.system(r"allure generate -c -o allure-report")  # add assertion here


if __name__ == '__main__':
    unittest.main()
