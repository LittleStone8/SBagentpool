# coding:utf-8
from bs4 import BeautifulSoup
from framemodule.Parser import Parser


class xiciparser(Parser):
    def __init__(self):
        pass

    # 解析xici数据
    def parse(self, page_url, html_cont):
        parseIpset=set();
        soup = BeautifulSoup(html_cont, "html.parser")
        all = soup.find_all('tr', class_='odd')
        for i in all:
            t = i.find_all('td')
            ip = t[1].text + ':' + t[2].text
            parseIpset.add(ip)
        return parseIpset

    pass


