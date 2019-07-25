# coding:utf-8
#

from agentpool.agentcraw.seleniumer import seleniumerCommon
from framemodule.UrlManager import UrlManager

class SeleniumerUrlmanager(UrlManager):
    def __init__(self):
        self.new_urls_66=set()
        self.url_xpath_66= seleniumerCommon.seleniumer_url_xpath_66

        self.new_urls_kuaidaili = set()
        self.url_xpath_kuaidaili = seleniumerCommon.seleniumer_url_xpath_kuaidaili
        pass

    #获取66网站地址
    def get_new_url_66(self):
        self.new_urls_66.clear()
        for m in range(1, seleniumerCommon.seleniumer_url_66_max_page):
            url_66 = seleniumerCommon.seleniumer_url_66 % (m)
            self.new_urls_66.add(url_66)
        return self.new_urls_66

    pass

    # 获取快代理网站地址
    def get_new_url_kuaidaili(self):
        self.new_urls_kuaidaili.clear()
        for m in range(1, seleniumerCommon.seleniumer_url_kuaidaili_max_page):
            url_kuaidaili = seleniumerCommon.seleniumer_url_kuaidaili % (m)
            self.new_urls_66.add(url_kuaidaili)
        return self.new_urls_66
    pass

