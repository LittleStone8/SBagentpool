# coding:utf-8
import configparser
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("SBagentpool\\")+len("SBagentpool\\")]  # 获取myProject，也就是项目的根路径
conf = configparser.ConfigParser()
conf.read(rootPath+'\\cofig.ini')


class SchedulerCommon:
    def __init__(self):
        self.main_thread_pool_size = conf.getint('scheduler', 'main_thread_pool_size')
        self.second_thread_pool_size = conf.getint('scheduler', 'second_thread_pool_size')
        self.third_thread_pool_size = conf.getint('scheduler', 'third_thread_pool_size')
        self.fourth_thread_pool_size = conf.getint('scheduler', 'fourth_thread_pool_size')
        self.agentmanager_thread_pool_size = conf.getint('scheduler', 'agentmanager_thread_pool_size')

    pass


schedulercommonObject=SchedulerCommon()
main_thread_pool_size=schedulercommonObject.main_thread_pool_size
second_thread_pool_size=schedulercommonObject.second_thread_pool_size
third_thread_pool_size=schedulercommonObject.third_thread_pool_size
fourth_thread_pool_size=schedulercommonObject.fourth_thread_pool_size
agentmanager_thread_pool_size=schedulercommonObject.agentmanager_thread_pool_size
