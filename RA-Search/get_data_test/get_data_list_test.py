# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

'''
获取列表页面数据
'''

# 使用本地Chrome浏览器访问，还支持其他浏览器 譬如Firefox
browser = webdriver.Chrome()
url = 'http://app1.sfda.gov.cn/datasearchcnda/face3/search.jsp?tableId={0}&curstart={1}'
url = url.format(26,1)
browser.get(url)  # Load page
time.sleep(1)  # Let the page load

#获得网页数据
data = browser.page_source

browser.close()


