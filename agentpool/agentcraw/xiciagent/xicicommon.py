# coding:utf-8
import configparser
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("SBagentpool\\")+len("SBagentpool\\")]  # 获取myProject，也就是项目的根路径
conf = configparser.ConfigParser()
conf.read(rootPath+'\\cofig.ini')

#西刺网址
class xici_url_common:
    def __init__(self):
        domestic_general_agent = conf.get('xiciurl', 'domestic_general_agent')
        domestic_high_altitude_agent = conf.get('xiciurl', 'domestic_high-altitude_agent')
        domestic_https_agent = conf.get('xiciurl', 'domestic_https_agent')
        doreign_http_agent = conf.get('xiciurl', 'doreign_http_agent')
        craw_xici_max_page = conf.getint('xiciurl', 'craw_xici_max_page')
        xici_max_quest_timeout = conf.getint('xiciurl', 'xici_max_quest_timeout')
        check_targeturl=conf.get('xiciurl', 'check_targeturl')
        xici_craw_interval = conf.getint('xiciurl', 'xici_craw_interval')
        checkip_max_quest_timeout = conf.getint('xiciurl', 'checkip_max_quest_timeout')

        self.servers = set()
        self.list = {'1': domestic_general_agent,  # xicidaili国内普通代理
                '2': domestic_high_altitude_agent,  # xicidaili国内高匿代理
                '3': domestic_https_agent,  # xicidaili国内https代理
                '4': doreign_http_agent}  # xicidaili国外http代理
        self.max_page=craw_xici_max_page
        self.quest_timeout = xici_max_quest_timeout
        self.check_targeturl = check_targeturl
        self.xici_craw_interval=xici_craw_interval
        self.checkip_max_quest_timeout=checkip_max_quest_timeout

    pass
xiciurlcommonObject=xici_url_common()
xici_url_list = xiciurlcommonObject.list # 初始化结构对象
xici_max_page = xiciurlcommonObject.max_page
xici_max_quest_timeout = xiciurlcommonObject.quest_timeout
xici_check_targeturl =xiciurlcommonObject.check_targeturl
xici_craw_interval=xiciurlcommonObject.xici_craw_interval
checkip_max_quest_timeout=xiciurlcommonObject.checkip_max_quest_timeout
