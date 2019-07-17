#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import time
import Queue

'''
该示例，模拟多线程获取数据；
思路如下：
1、在队列里存取100个数
2、启动10个线程，同时从队列里取数（每取1次，休眠一秒）
3、多线程启动时，一共需要10秒就能同时把队列数据取完
'''




'''
初始化一个全局队列，并1~100加入队列
'''
q = Queue.Queue()
def initData():
    for i in range(100):
        q.put(i)


'''
从队列获取数据
'''
def get_data():
    if not q.empty():
        return q.get()
    return -1


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print "====Starting " + self.name
        print_data(self.name)
        print "====Exiting " + self.name


def print_data(threadName):
    while True:
        i = get_data()
        if i == -1:
            break
        #每取出1个数，休眠1秒
        time.sleep(1)
        print(threadName +  "   get data:    "+str(i) + "\n")


if __name__ == "__main__":
    initData()
    threads = []

    begin = time.time()
    # 创建10个线程
    for i in range(10):
        thread = myThread(i, "Thread-" + str(i))
        # 添加线程到线程列表、并立即启动线程
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for t in threads:
        t.join()
        end = time.time()
    print "total time: %ds" % int(end - begin)
    print "Exiting Main Thread"

