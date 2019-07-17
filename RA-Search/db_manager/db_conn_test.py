#coding=utf-8
__author__ = 'wenglin'
#==========
# 数据库连接测试
#==========

#导入pymysql的包
import pymysql

conn =  pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='1qaz$ESZ',
        db='mysql',
        charset='utf8'
    )
cur = conn.cursor()

try:
    cur.execute('select * from user')
    data=cur.fetchall()

    print '信息查询成功，mysql.user表用户信息如下:'
    for d in data :
        print 'mysql用户名: ' + str(d[1])

    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
except  Exception :print("发生异常")