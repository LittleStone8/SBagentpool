# coding:utf-8
import configparser
import os
from selenium import webdriver

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("SBagentpool\\")+len("SBagentpool\\")]  # 获取myProject，也就是项目的根路径
conf = configparser.ConfigParser()
conf.read(rootPath+'\\cofig.ini')


class SeleniumerCommon:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.options.add_argument('disable-infobars')
        self.prefs = {
            'profile.default_content_setting_values': {
                'images': 2
            }
        }
        self.options.add_experimental_option('prefs', self.prefs)#不加载图片

        self.page_load_timeout=conf.getint('seleniumer', 'page_load_timeout')
        self.script_timeout=conf.getint('seleniumer', 'script_timeout')
        self.implicitly_wait=conf.getint('seleniumer', 'implicitly_wait')
        self.checkip_max_quest_timeout = conf.getint('seleniumer', 'checkip_max_quest_timeout')
        self.check_targeturl = conf.get('seleniumer', 'check_targeturl')
        self.url_66 = conf.get('seleniumer', 'url_66')
        self.url_xpath_66 = conf.get('seleniumer', 'url_xpath_66')
        self.url_66_max_page = conf.getint('seleniumer', 'url_66_max_page')
        self.url_66_craw_interval = conf.getint('seleniumer', 'url_66_craw_interval')

        self.url_xpath_kuaidaili = conf.get('seleniumer', 'url_xpath_kuaidaili')
        self.url_kuaidaili = conf.get('seleniumer', 'url_kuaidaili')
        self.url_kuaidaili_max_page = conf.getint('seleniumer', 'url_kuaidaili_max_page')
        self.url_kuaidaili_craw_interval = conf.getint('seleniumer', 'url_kuaidaili_craw_interval')

        self.url_zhandaye = conf.get('seleniumer', 'url_zhandaye')
        self.url_xpath_zhandaye = conf.get('seleniumer', 'url_xpath_zhandaye')
        self.url_zhandaye_craw_interval = conf.getint('seleniumer', 'url_zhandaye_craw_interval')
    pass
seleniumerCommonObject=SeleniumerCommon()
seleniumer_options=seleniumerCommonObject.options
seleniumer_page_load_timeout=seleniumerCommonObject.page_load_timeout
seleniumer_script_timeout=seleniumerCommonObject.script_timeout
seleniumer_implicitly_wait=seleniumerCommonObject.implicitly_wait
seleniumer_checkip_max_quest_timeout=seleniumerCommonObject.checkip_max_quest_timeout
seleniumer_check_targeturl=seleniumerCommonObject.check_targeturl
#66
seleniumer_url_66=seleniumerCommonObject.url_66
seleniumer_url_xpath_66=seleniumerCommonObject.url_xpath_66
seleniumer_url_66_max_page=seleniumerCommonObject.url_66_max_page
seleniumer_url_66_craw_interval=seleniumerCommonObject.url_66_craw_interval
#kuaidaili
seleniumer_url_kuaidaili=seleniumerCommonObject.url_kuaidaili
seleniumer_url_xpath_kuaidaili=seleniumerCommonObject.url_xpath_kuaidaili
seleniumer_url_kuaidaili_max_page=seleniumerCommonObject.url_kuaidaili_max_page
seleniumer_url_kuaidaili_craw_interval=seleniumerCommonObject.url_kuaidaili_craw_interval
#zhandaye
seleniumer_url_zhandaye=seleniumerCommonObject.url_zhandaye
seleniumer_url_xpath_zhandaye=seleniumerCommonObject.url_xpath_zhandaye
seleniumer_url_zhandaye_craw_interval=seleniumerCommonObject.url_zhandaye_craw_interval