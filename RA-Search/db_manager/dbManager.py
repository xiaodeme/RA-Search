#coding=utf-8
import MySQLdb
from test import DataInfo

import sys
reload(sys)

import logging
logging.basicConfig(filename='E:/data/cfda/table26/logs/dbManager.log',format='%(asctime)s - %(levelname)s - %(message)s',level=logging.ERROR)


sys.setdefaultencoding('utf-8')
db =  MySQLdb.connect(
        host='127.0.0.1',
        port=3306,
        user='RA',
        passwd='12345qwert',
        db='RASearchDB',
        charset='utf8'
    )
# prepare a cursor object using cursor() method
cursor = db.cursor()
#
# 插入数据对象
#
def insertDataInfo(dataInfo,commitFlag):
    try:
        # sql = "INSERT INTO data_info(DATA_OTHER_ID,DATA_TYPE,PRODUCT_NAME,COMPANY_NAME,REGISTER_CODE) \
        #            VALUES ('%s', '%s', '%s', '%s' , '%s');" % \
        #       (dataInfo.data_other_id,dataInfo.data_type,dataInfo.product_name,dataInfo.company_name,dataInfo.register_code)
        # # print(sql)

        #采用两个参数的方法，会自动将特殊字符转义. 参考：https://my.oschina.net/u/2000675/blog/808264
        sql = "insert into data_info(DATA_OTHER_ID,DATA_TYPE,PRODUCT_NAME,COMPANY_NAME,REGISTER_CODE) values(%s, %s, %s, %s, %s)"
        param = (dataInfo.data_other_id,dataInfo.data_type,dataInfo.product_name,dataInfo.company_name,dataInfo.register_code);

        cursor.execute(sql,param)
        print("dataInfo保存成功")

        if commitFlag == 1:
            db.commit()
            print("dataInfo正式提交到数据库")


        return  cursor.lastrowid

    except BaseException as e:
        db.rollback()
        print("===========exception============")
        print(sql)
        print("insertDataInfo出现异常");
        print(e)

        logging.error("insertDataInfo出现异常")
        logging.error(e)
        # disconnect from server
        db.close()


#
# 插入数据属性对象(使用批量提交)
#
def insertDataDescInfo(param,commitFlag):
    try:
        sql = 'insert into data_desc_info(DATA_ID,DESC_DEFINE_ID,DESC_VALUE) values(%s, %s, %s)'
        cursor.executemany(sql,param)
        print("dataDescInfo保存成功:"+str(commitFlag))

        if commitFlag == 1:
            db.commit()
            print("dataDescInfo正式提交到数据库")


    except BaseException as e:
        db.rollback()

        print("===========exception============")
        print(param)
        print("insertDataDescInfo出现异常");
        print(e)
        # disconnect from server
        db.close()

if __name__ == "__main__":

    pass
