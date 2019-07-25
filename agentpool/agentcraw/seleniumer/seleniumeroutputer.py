# coding:utf-8
import json
import time

from agentpool.agentcraw.seleniumer import seleniumerCommon
from agentpool.agentcraw.seleniumer.seleniumerloader import Seleniumerloader
from agentpool.bean.agent_info import agent_info
from framemodule.Outputer import Outputer
from thirdpartytool.redis.redisutil import redisutil


class Seleniumeroutputer(Outputer):
    def __init__(self):
        pass

    def collect_data(self, data,url,angentsrc):
        storageset=set()
        storagesum=0
        if data == None:
            return storagesum
        for ip in data:
            if redisutil.hashexists(ip)==True:
                continue
            storagesum=storagesum+1
            starttime=time.time()
            if True==Seleniumerloader.checkip1(seleniumerCommon.seleniumer_check_targeturl, ip):
                endtime = time.time()
                add_agent=agent_info(ip,None,time.time(),1, starttime,angentsrc,endtime-starttime,30)
                storageset.clear()
                storageset.add(add_agent)
                self.collect_data_to_redis(storageset) ##
            else:
                endtime = time.time()
                add_agent=agent_info(ip,None,time.time(),1, starttime,angentsrc,endtime-starttime,50)
                storageset.clear()
                storageset.add(add_agent)
                self.collect_data_to_redis(storageset) ##
        return storagesum
        pass


    def collect_data_to_mysql(self, data):
        pass

    def collect_data_to_redis(self, data):
        for agent_info_temp in data:
            json_str = json.dumps(agent_info_temp,default=lambda obj: obj.__dict__,sort_keys=True)
            redisutil.sortedsetZADD(agent_info_temp.score,agent_info_temp.ip)
            redisutil.hashset(agent_info_temp.ip,json_str)
        pass

    def collect_data_to_print(self, data):

        pass
