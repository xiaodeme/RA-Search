#coding=utf-8

'''
数据采集主函数
'''
from utils import  const
from utils import  utils
from data_manager import get_data_list as data_list
import sys





if __name__ == "__main__":
    print ('======数据获取========begin==')
    tips = "===============================\n" \
           "数据抓取需要配置如下信息：\n" \
           "1) 数据保存根路径:root_dir \n" \
           "2) 器械标识:tableId \n" \
           "3) 器械标识对应数据总数量:totalCount\n" \
           "==============================="

    '''
        root_dir:文件存储磁盘根路径
        tableId:器械标识(查询所得) 如上
        totalCount:器械总数量(这里器械总行数网页查询所得http://app1.sfda.gov.cn/datasearchcnda/face3/dir.html?type=ylqx)
    '''

    root_dir = "E:/data/nmpa_data/"
    tableId = 26
    totalCount = 1

    # 参数校验
    r = utils.is_path_ok(root_dir)
    if r == False or not str(tableId).strip() or not str(totalCount).strip() or totalCount <= 0:
        print (tips)
        sys.exit(0)

    # 日志配置
    log_dir = root_dir + "table" + str(tableId) + "/logs/"
    utils.logConfig(log_dir, "get_data.log")

    print ('器械列表数据获取========begin==')
    data_list.save_data_to_disk(tableId, totalCount, root_dir)
    print ('器械列表数据获取========end==')




    print ('======数据获取========end==')
