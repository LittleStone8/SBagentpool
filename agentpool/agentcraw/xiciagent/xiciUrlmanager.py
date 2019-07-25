# coding:utf-8
#
from agentpool.agentcraw.xiciagent import xicicommon
from framemodule.UrlManager import UrlManager


class xiciUrlmanager(UrlManager):
    def __init__(self):
        for type in range(len(xicicommon.xici_url_list)):  # 四种类型ip,每种类型取前三页,共12条线程
            for pagenum in range(xicicommon.xici_max_page):
                url = xicicommon.xici_url_list[str(type + 1)] + str(pagenum + 1)  # 配置url
                self.new_urls.add(url)
        pass

''''
# 主启动程序
if __name__=="__main__":
    obj_spider = xiciUrlmanager()
    print(len(obj_spider.new_urls))
    print(obj_spider.get_new_url())
    print(getheaders())
'''''

