# -*- coding: utf-8 -*-

'''
==============================
相关说明
主要要获取如下器械标识数据
器械标识(根据URL查询分析所得)
==============================
25 国产药品
36 进口药品
26 国产器械
27 进口器械
68 国产特殊用途化妆品
69 进口化妆品
'''


"""
每页显示总数量(即每个文件保存1000条数据)
"""
PAGE_SIZE_MAX = 1000


#数据列表保存文件名称
DATA_LIST_FOLDER_NAME = '/list/'

#数据列表URL地址
'''
一共有3个参数
pageIndex 当前页码
pageSize  返回数据总量 不宜设定过大 <= 1000即可，不要把网址搞垮了
tableId   数据类型标识,详见const文件顶部说明
'''
DATA_LIST_URL = 'http://mobile.cfda.gov.cn/datasearch/QueryList?pageIndex={0}&pageSize={1}&tableId={2}'



'''
TABLE_ID = []

ROOT_DIR = 'E:\data'

DATA_TYPE_26 = 26 #国产医疗器械

DATA_TYPE_26_COUNT = 157011  #国产医疗器械当前数据库总数量

DATA_TYPE_26_DATA_PATH = ''


DATA_TYPE_27 = 27 #进口医疗器械

DATA_TYPE_27_COUNT = 52147   #进口医疗器械当前数据库总数量
'''