# coding:utf-8
import re

from framemodule.Parser import Parser


class zhandayeparser(Parser):
    def __init__(self):
        pass

    # 解析站大爷数据
    def parse(self, page_url, html_cont):
        parseIpset=set();
        p = r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\D+?(?:6[0-5]{2}[0-3][0-5]|[1-5]\d{4}|[1-9]\d{1,3}|[0-9])\b"
        iplist = re.findall(p, html_cont)
        for ip in iplist:
            parseIpset.add(ip)
        return parseIpset
    pass


