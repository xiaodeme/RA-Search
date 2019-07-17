#coding=utf-8
import os
import json
import  logging

def logConfig(log_name):
    # output format: output time - logging level - log messages
    logging.basicConfig(filename=log_name, format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)


#写入json文件到磁盘
def writeFileToJson(file_path,data):
    with open(file_path,"w") as f:
        f.write(json.dumps(data))
        print("属性文件写入成功")
    return True


'''
写入文件到磁盘
file:写入文件路径 e:/data/test.txt
data:写入文件内容
'''
def write_file(file,data):
    try:
        with open(file, "w") as f:
            f.write(data)
        return True
    except Exception:
        return False


""" 文件是否存在 """
def fileIsExist(file_path):
    return os.path.exists(file_path)

'''
获取当前已经存储最大数
'''
def get_curr_max_pageno(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            # print(file[0:file.index(".")])
            L.append(file[0:file.index(".")])


    if len(L) == 0:
        return 1
    else:
        max_pageno = len(L)
        return max_pageno

'''
判断路径是否正确
'''
def is_path_ok(root_dir):
    try:
        t = root_dir[len(root_dir) - 1:]
        if t.index("/") == 0:
            return True
    except ValueError as e:
            print("请设置正确路径：注意最后的反斜杠:{0}".format(root_dir))
            print("正确示例 /home/data/")
            print("错误示例 /home/data")
            return False

#获取文件路径集合
def getFilenameList(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            L.append(os.path.join(root, file))
    return L


#创建路径
def mkdir_path(foderPath):
    if os.path.exists(foderPath) == False:
        os.makedirs(foderPath)
    return True


#统计detial文件夹下获取到数据总数
def dataTotalCount(root_dir,tableId):
    tableName = "table" + str(tableId)
    detail_dir = root_dir + tableName+ "/detail"
    file_list = getFilenameList(detail_dir)
    count = 0
    for filename in file_list:
        print(filename)
        with open(filename, "r") as file:
            while 1:
                lines = file.readlines()
                if not lines:
                    break

                count += len(lines)

    return count
if __name__ == "__main__":

    # tableId= 36
    # root_dir = "E:/data/cfda2/"
    # count = dataTotalCount(root_dir,tableId)
    # print(count)

    pass