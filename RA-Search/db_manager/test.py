#coding=utf-8
import pymysql as MySQLdb
import urllib2
import datetime
import time
import json
import os
import sys
import Queue
import threading
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
db =  MySQLdb.connect(
        host='127.0.0.1',
        port=3306,
        user='cfda',
        passwd='12345qwert',
        db='cfdadb',
        charset='utf8'
    )
# prepare a cursor object using cursor() method
cursor = db.cursor()


class DataInfo():
    def __init__(self,data_other_id=None,data_type=None,product_name=None,company_name=None,register_code=None):
        self.data_other_id = data_other_id
        self.data_type = data_type
        self.product_name=product_name
        self.company_name=company_name
        self.register_code=register_code

class DataDescInfo():
    def __init__(self,data_id=None,desc_define_id=None,desc_value=None):
        self.data_id = data_id
        self.desc_define_id = desc_define_id
        self.desc_value = desc_value





def get_detail_data_attribute(value):
    pass
def file_name(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            L.append(os.path.join(root, file))
    return L


def save_detail_data(file_path):
    with open(file_path, "r") as file:
        while 1:
            lines = file.readlines()
            if not lines:
                break

            totalRows = len(lines)
            return totalRows


def test(p1):
    print("输入%d,"%(p1))
    if p1 == 1:
        print("输入1 退出")
        return
    print("输入1 这里不应该执行")


if __name__ == "__main__":
    test(2)

    # write_detail_data_attribute()


    # dist = {}
    # with open("E:/data/cfda/table26/opt/key-value.json","r") as f:
    #     line = f.readline()
    #     dist = json.loads(line,encoding="utf-8")
    #
    # for x in dist:
    #     # print(x + "==" + dist[x])
    #     sql = "INSERT INTO desc_define_info(DESC_DEFINE_CODE,DESC_DEFINE_NAME,DESC_NOTE,SORT_ID) \
    #                VALUES ('%s', '%s', '%s', '%d' );" % \
    #           (x,dist[x],"国产器械",int(x[3:]))
    #     print(sql)

    # t = dist["key20"]
    # print(str(t) == "预期用途（体外诊断试剂）  ".strip())

    ###############属性值存储国产器械
    # try:
    #     cursor.execute("select * from desc_define_info order by sort_id")
    #
    #     dataList = cursor.fetchall()
    #
    #     dist = {}
    #     for x in dataList:
    #         # print(x["DESC_DEFINE_NAME"])
    #         # print(x[2])
    #         dist[x[0]] = x[2]
    #
    #     print(dist)
    #     with open("E:/data/cfda/table26/opt/key-value2.json","w") as f:
    #         f.write(json.dumps(dist))
    #         print("属性文件写入成功")
    #
    # except:
    #     db.rollback()
    #     print("失败");
    #     # disconnect from server
    # db.close()

        # d = DataDescInfo(111,2,3)
        # print(d.data_id)
        #
        # d.data_id = 222
        # print(d.data_id)

    # base_dir = "E:/data/cfda2/table36"
    #
    #
    # # 2.分析入库
    # detail_dir = base_dir + "/detail"
    # file_list = file_name(detail_dir)
    # count= 0
    # for file in file_list:
    #     # print(file + "开始分析入库==begin!")
    #     count  += save_detail_data(file)
    #
    # print(count)
    # totalCount = 100
    # msg1 = "计划获取数据 %d"% (totalCount)
    # print msg1
    #
    # print ("统计信息 %s" % ("Aviad"))
    #
    # print ("统计信息 %d" % (50))