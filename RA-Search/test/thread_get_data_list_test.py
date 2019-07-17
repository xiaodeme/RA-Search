# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import  sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import Queue
import threading


q = Queue.Queue()
FILE_SAVE_ROOT = 'E:/data/nmpa_data/'

#写入json文件到磁盘
def writeFile(file_name,data):
    f = FILE_SAVE_ROOT+file_name
    print(f)
    with open(f,"w") as f:
        f.write(data)
        print("文件写入成功")
    return True


def init_data():
    # total_count = 158908
    total_page_count = 10589

    startIndex = 10589
    endIndex = total_page_count + 1

    for x in range(10590,10595):
        q.put(x)
    print("加入队列总页数：" + str(q.qsize()))










class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self,thread_name):
        threading.Thread.__init__(self)
        self.thread_name = thread_name

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        msg1 = "====Starting " + self.name
        print(msg1)

        get_data_list(self.name)

        msg2 = "====Exiting " + self.name
        print(msg2)


    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False





#从cfda数据库抓取数据
def get_data_list(threadName):
    while not q.empty():
        try:
            curstart = q.get()
            notGetDataCountInfo = "线程名:%s,没有获取到数据还有 %d个" % (threadName,q.qsize())
            print(notGetDataCountInfo)

            option = webdriver.ChromeOptions()
            option.add_argument("headless")
            browser = webdriver.Chrome(chrome_options=option)

            url = 'http://app1.sfda.gov.cn/datasearchcnda/face3/search.jsp?tableId={0}&curstart={1}'


            url = url.format(26,curstart)
            print(url)

            browser.get(url)  # Load page
            time.sleep(1)  # Let the page load

            #获得网页数据
            data = browser.page_source
            writeFile(str(curstart)+".html",data)

            # browser.close()
            browser.quit()
        except BaseException as e:
            print("BaseException")




if __name__ == "__main__":

    init_data()
    print("====初始化数据完成=====")


    threadCount = 5
    # 启动60个线程，如果cfda官网服务拒绝链接，可适当将线程数量调小一点
    threads = []
    for i in range(threadCount):
        thread = myThread("Thread-" + str(i))  # 区分其他线程名字
        # 添加线程到线程列表
        threads.append(thread)

    for t in threads:
        t.start()

    # # 等待所有线程完成
    for t in threads:
        if t.isAlive():
            t.join()
    print "所有线程全部结束!"











