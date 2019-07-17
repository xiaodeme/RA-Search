# -*- coding: utf-8 -*-

import os

#10594

'''
获取当前已经存储最大数
'''
def get_curr_max_pageno(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            L.append(file[0:file.index(".")])
    if len(L) == 0:
        return 1
    else:
        max_pageno = int(max(L)) + 1
        return max_pageno


if __name__ == "__main__":
    t =  get_curr_max_pageno('E:/data_source2/26/list/')
    # print t
    total_page_count  = 5

    startIndex = int(t)
    endIndex = total_page_count + 1
    for x in range(startIndex , endIndex):
        print x