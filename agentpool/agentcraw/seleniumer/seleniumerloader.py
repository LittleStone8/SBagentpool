# coding:utf-8
import random
import time

import requests

from agentpool.agentcraw.seleniumer import seleniumerCommon
from agentpool.agentmanager import agentmanagerutil, agentmanagercommon
from common.httpheader import getheaders
from framemodule.Downloader import Downloader
from selenium import webdriver


class Seleniumerloader(Downloader):
    url_xpath_66 = '//*[@id="footer"]/div/table/tbody/tr[position()>1]'


    def download_by_myself(self, url,url_xpath,proxies):
        agentmanagercommon.agentmanager_requestsum = agentmanagercommon.agentmanager_requestsum + 1
        try:
            if proxies!=None:
                seleniumerCommon.seleniumer_options.add_argument('--proxy-server=http://%s' % proxies)
                agentmanagercommon.agentmanager_use_proxy_time = agentmanagercommon.agentmanager_use_proxy_time + 1
            else :
                agentmanagercommon.agentmanager_use_myself_time=agentmanagercommon.agentmanager_use_myself_time+1
            browser = webdriver.Chrome(options=seleniumerCommon.seleniumer_options)
            browser.set_page_load_timeout(seleniumerCommon.seleniumer_page_load_timeout)
            browser.set_script_timeout(seleniumerCommon.seleniumer_script_timeout)  # 这两种设置都进行才有效
            browser.implicitly_wait(seleniumerCommon.seleniumer_implicitly_wait)
            proxy_list = set()
            browser.get(url)

            # 找到代理table的位置
            elements = browser.find_elements_by_xpath(url_xpath)
            for element in elements:
                ip = element.find_element_by_xpath('./td[1]').text
                port = element.find_element_by_xpath('./td[2]').text
                ip_addr = ip + ':' + port
                proxy_list.add(ip_addr)
            browser.quit()
            return proxy_list
        except Exception as e:
            return None
    pass

    def download_by_myself_useagent(self, url,url_xpath):
        proxiesips=agentmanagerutil.agentmanagerutil.providing_quality_proxie()
        retain_proxy_list=None
        for proxiesipstr in proxiesips:
            if proxiesips ==None:
                continue
            else:
                proxy_list = self.download_by_myself(url, url_xpath, proxiesipstr)
                if (proxy_list != None and len(proxy_list) != 0):
                    agentmanagerutil.agentmanagerutil.use_updates_proxie(proxiesipstr, True)
                    agentmanagercommon.agentmanager_use_proxy_success_time=agentmanagercommon.agentmanager_use_proxy_success_time+1
                    return proxy_list
                if (proxy_list != None and len(proxy_list) == 0):
                    retain_proxy_list=proxy_list
                if proxy_list==None:
                    agentmanagerutil.agentmanagerutil.use_updates_proxie(proxiesipstr, False)
            time.sleep(0.1)
        if retain_proxy_list!=None:
            return retain_proxy_list
        return self.download_by_myself(url,url_xpath,None)
    pass

    def checkip(self,targeturl1,ip):
        headers =getheaders()  # 定制请求头
        proxies = {"http": "http://"+ip, "https": "http://"+ip}  # 代理ip
        try:
            response=requests.get(url=targeturl1, proxies=proxies, headers=headers, timeout=seleniumerCommon.seleniumer_checkip_max_quest_timeout).status_code
            if response == 200 :
                return True
            else:
                return False
        except:
            return False
    pass

    def checkip1(targeturl1,ip):
        headers =getheaders()  # 定制请求头
        proxies = {"http": "http://"+ip, "https": "http://"+ip}  # 代理ip
        try:
            response=requests.get(url=targeturl1, proxies=proxies, headers=headers, timeout=seleniumerCommon.seleniumer_checkip_max_quest_timeout).status_code
            if response == 200 :
                return True
            else:
                return False
        except:
            return False
    pass