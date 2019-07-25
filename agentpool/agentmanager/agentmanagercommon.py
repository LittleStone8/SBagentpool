# coding:utf-8
import configparser
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("SBagentpool\\")+len("SBagentpool\\")]  # 获取myProject，也就是项目的根路径
conf = configparser.ConfigParser()
conf.read(rootPath+'\\cofig.ini')

class agentmanager_common:
    def __init__(self):
        ####计数不做线程安全控制，仅供参考
        self.requestsum = 0  # 对外请求总量
        self.use_myself_time = 0 #使用自身Ip进行请求次数
        self.use_proxy_time=0  #使用代理次数
        self.use_proxy_success_time = 0 #使用代理成功次数


        self.agentmanager_worst_score = 100  # 最坏代理的打分的分数
        self.agentmanager_worst_block = 500  # 表示清理最坏的代理时多少个占用一条线程
        self.agentmanager_routine_block = 500
        self.domestic_general_agent = conf.get('agentmanager', 'agentmanager_worst_score')
        self.checkurls=[]
        self.baiduurl = 'https://www.baidu.com/'  # 百度
        self.cbgurl = 'https://xyq.cbg.163.com/'  # cbg
        self.mhurl = 'http://xyq.163.com/'  # MH
        self.zhihuurl = 'https://www.zhihu.com/'  # zhihu
        self.zhangzongurl = 'https://gitee.com/zhso'  # 张总git
        self.checkurls.append(self.baiduurl)
        self.checkurls.append(self.cbgurl)
        self.checkurls.append(self.mhurl)
        self.checkurls.append(self.zhihuurl)
        self.checkurls.append(self.zhangzongurl)
        self.checkip_max_timeout=5
        self.error_quest_score = 15
        self.abandon_time = 60 * 60 * 24 * 7 #一个星期请求不成功则抛弃
        self.abandon_score = 100
        self.full_penalty_score=self.abandon_score-(self.error_quest_score*len(self.checkurls)) #惩罚分满分
    pass
agentmanagercommonObject=agentmanager_common()
agentmanager_worst_score = agentmanagercommonObject.agentmanager_worst_score
agentmanager_worst_block = agentmanagercommonObject.agentmanager_worst_block
agentmanager_checkurls = agentmanagercommonObject.checkurls
agentmanager_checkip_max_timeout=agentmanagercommonObject.checkip_max_timeout
agentmanager_error_quest_score=agentmanagercommonObject.error_quest_score
agentmanager_routine_block=agentmanagercommonObject.agentmanager_routine_block
agentmanager_abandon_time=agentmanagercommonObject.abandon_time
agentmanager_full_penalty_score=agentmanagercommonObject.full_penalty_score
agentmanager_requestsum=agentmanagercommonObject.requestsum
agentmanager_use_myself_time=agentmanagercommonObject.use_myself_time
agentmanager_use_proxy_time=agentmanagercommonObject.use_proxy_time
agentmanager_use_proxy_success_time=agentmanagercommonObject.use_proxy_success_time