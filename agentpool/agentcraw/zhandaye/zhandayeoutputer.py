# coding:utf-8
import json
import time

from agentpool.bean.agent_info import agent_info
from agentpool.agentcraw.xiciagent import xicicommon
from agentpool.agentcraw.xiciagent.xicidownloader import xicidownloader
from framemodule.Outputer import Outputer
from thirdpartytool.redis.redisutil import redisutil


class zhandayeoutputer(Outputer):
    def __init__(self):
        pass

    def collect_data(self, data,url,angentsrc):
        availset=set()
        storagesum = 0
        if data == None:
            return storagesum
        for ip in data:
            if redisutil.hashexists(ip)==True:
                continue
            storagesum=storagesum+1
            starttime=time.time()
            if True==xicidownloader.checkip(xicicommon.xici_check_targeturl, ip):
                endtime = time.time()
                add_agent=agent_info(ip,None,time.time(),1, starttime,angentsrc,endtime-starttime,25)
                availset.clear()
                availset.add(add_agent)
                self.collect_data_to_redis(availset) ##
            else:
                endtime = time.time()
                add_agent=agent_info(ip,None,time.time(),1, starttime,angentsrc,endtime-starttime,50)
                availset.clear()
                availset.add(add_agent)
                self.collect_data_to_redis(availset) ##
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
