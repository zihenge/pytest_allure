# coding=gbk
import pandas

from utils.ConfigParserUtils import ConfigParserUtils


class ReadFileUtils:

    # Ŀǰֻ֧��ȫ·�� ����ȫ·��
    # 'C:\Users\DELL\PycharmProjects\pythonProject\sources\userIdsList'
    def readCsvFile(self, file_name):
        userIdList = []
        fileopen = open(str(file_name), 'r+')
        readlines = fileopen.readlines()
        for lins in readlines:
            userIdList.append(lins.replace('\n',''))
        return userIdList
