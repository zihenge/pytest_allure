"""
    公共方法
"""
import random

import yaml

class DebugTalk:
    #获取随机数的方法
    def get_tandom_number(self,min,max):
        return random.randint(int(min),int(max))