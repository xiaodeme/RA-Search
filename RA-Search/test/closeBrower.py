from selenium import webdriver
option = webdriver.ChromeOptions()

option.add_argument("headless")
browser = webdriver.Chrome(chrome_options=option)


browser.get("http://app1.sfda.gov.cn/datasearchcnda/face3/search.jsp?tableId=26&curstart=1")

print browser.page_source
print(browser.title)
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
# print(driver.title)
#

browser.quit()
