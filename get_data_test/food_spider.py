# -*- coding: utf-8 -*-
import scrapy, random,time




from selenium import webdriver


class FoodSpiderSpider(scrapy.Spider):
    name = "food_sc"

    def __init__(self):
        chrome_option = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_option.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(
            executable_path=r"C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe",
            chrome_options=chrome_option
        )
        self.driver.set_window_size(1440, 900)
        self.driver.set_page_load_timeout(20)

    def start_requests(self):

        for kw in range(35680, 50000):  # 152937

            print('------当前搜索到许可证id为------%s------' % kw)
            url = "http://qy1.sfda.gov.cn/datasearch/face3/content.jsp?tableId=120&tableName=TABLE120&tableView=食品生产许可获证企业(SC)&Id=%d" % kw
            # url ="http://httpbin.org/ip"
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        try:
            item = fpItem()
            # datas = response.css('table:nth-child(1) tr td:nth-child(2)::text').extract()
            datass = response.css('table:nth-child(1) tr td:nth-child(2)').extract()
            # print(datass)
            if len(datass) >3:
                producer_name = datass[0].replace('</td>', '').replace('<td bgcolor="#eaeaea" width="83%">', '') #生产者名称
                code_num = datass[1].replace('</td>', '').replace('<td bgcolor="#ffffff" width="83%">', '')#社会信用代码
                legal_person = datass[2].replace('</td>', '').replace('<td bgcolor="#eaeaea" width="83%">', '')#法定代表人
                residence = datass[3].replace('</td>', '').replace('<td bgcolor="#ffffff" width="83%">', '')#住所
                production_address = datass[4].replace('</td>', '').replace('<td bgcolor="#eaeaea" width="83%">', '')#生产地址
                food_category = datass[5].replace('</td>', '').replace('<td bgcolor="#ffffff" width="83%">', '')#食品类别
                license_num = datass[6].replace('</td>', '').replace('<td bgcolor="#eaeaea" width="83%">', '')#许可证编号
                management_organization = datass[7].replace('</td>', '').replace('<td bgcolor="#ffffff" width="83%">',#日常监督机构
                                                                                 '')
                management = datass[8].replace('</td>', '').replace('<td bgcolor="#eaeaea" width="83%">', '')#日常监督管理人员
                certification_authority = datass[9].replace('</td>', '').replace('<td bgcolor="#ffffff" width="83%">',
                                                                                 '')#发证机关
                lssur = datass[10].replace('</td>', '').replace('<td bgcolor="#eaeaea" width="83%">', '')#签发人
                date_of_issue = datass[11].replace('</td>', '').replace('<td bgcolor="#ffffff" width="83%">', '')
                effective_date = datass[12].replace('</td>', '').replace('<td bgcolor="#eaeaea" width="83%">', '')
                detailed = datass[13].replace('</td>', '').replace('<br>', '\n').replace(
                    '<td bgcolor="#ffffff" width="83%">', '')

                item['producer_name'] = producer_name
                item['code_num'] = code_num
                item['legal_person'] = legal_person
                item['residence'] = residence
                item['production_address'] = production_address
                item['food_category'] = food_category
                item['license_num'] = license_num
                item['management_organization'] = management_organization
                item['management'] = management
                item['certification_authority'] = certification_authority
                item['lssur'] = lssur
                item['date_of_issue'] = date_of_issue
                item['effective_date'] = effective_date
                item['detailed'] = detailed
                item['source_type'] = 'sc'

                yield item
            else:
                print('--------该页数据并不存在--------')

        except Exception as e:
            print('获取数据时候出现错误，url：--{}--，错误是：--{}'.format(response.url, e))
            time.time(5)

    def closed(self, spider):
        print('spider closed')
        self.driver.close()
        msgs = self.name
        content = '爬取完成或者暂停中。。。。'
        email_spider(msgs, content)
