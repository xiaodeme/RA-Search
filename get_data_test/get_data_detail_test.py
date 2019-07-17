# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

'''
获取详情页面
'''

# 使用本地Chrome浏览器访问，还支持其他浏览器 譬如Firefox
browser = webdriver.Chrome()
url = 'http://app1.sfda.gov.cn/datasearchcnda/face3/search.jsp?tableId={0}&curstart={1}'
url = 'http://app1.sfda.gov.cn/datasearchcnda/face3/content.jsp?tableId={0}&tableName={1}&tableView={2}&Id={3}'


table_id = 26
table_name = "TABLE"+str(table_id)
tableView = '国产器械'
product_id=152656


url = url.format(table_id,table_name,tableView,product_id)


browser.get(url)  # Load page
time.sleep(1)  # Let the page load

print browser.page_source

browser.close()


