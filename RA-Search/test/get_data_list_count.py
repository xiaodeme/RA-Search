#coding=utf-8

import urllib2
import datetime
import time
import json
import os
import Queue
import threading
import logging
from utils import  utils
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#将cfda数据唯一标识存储到队列里面
q = Queue.Queue()

def getAllDataIds(filelist):
    for fileName in filelist:
        print(fileName)
        with open(fileName, "r") as f:
            jsonData = json.loads(f.read())
            for x in jsonData:
                q.put(x["ID"])
            print q.qsize()
    msg = "all data_id 都加入队列,初始化完成!"
    logging.info(msg)
    print(msg)

#获取data_list文件路径集合
def getFilenameList(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            L.append(os.path.join(root, file))
    return L


if __name__ == "__main__":

    #路径不能含有中文
    datalist_dir = 'E:/workspace/docment/RA-Search/CFDA_DB/table26/list/'
    data_file_list = utils.getFilenameList(datalist_dir)
    getAllDataIds(data_file_list)

    print(q.qsize())