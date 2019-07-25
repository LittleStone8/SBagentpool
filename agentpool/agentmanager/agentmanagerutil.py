import json
import math
import threading
import time

import requests

from agentpool.agentmanager import agentmanagercommon
from agentpool.bean.agent_info import agent_info
from thirdpartytool.redis import redisutil


class agentmanagerutil:
    def providing_quality_proxie(self,number=10):
        return redisutil.redisutil.sortedsetGETTOP(number)
    pass

    def updataoradd_proxie(self,agent_info):
        json_str = json.dumps(agent_info, default=lambda obj: obj.__dict__, sort_keys=True)
        hash_key = agent_info.ip
        redisutil.redisutil.sortedsetZADD(agent_info.score,agent_info.ip)
        redisutil.redisutil.hashset(hash_key, json_str)
    pass

    def updataoradd_proxiestr(self,ip,score,issuccess=False):
        redisob=redisutil.redisutil.hashget(ip)
        if redisob is None:
            agenttemp=agent_info(ip,0,time.time(),time.time(),time.time(),0,0,score)
            self.updataoradd_proxie(agenttemp)
        else :
            data = json.loads(redisob)
            penalty_score=0
            if issuccess==False:#加上惩罚分数
                if data['last_success_time'] is None:
                    data['last_success_time']=time.time()
                else:
                    penalty_score=self.calculate_penalty_time(data['last_success_time'])
            else:
                data['last_success_time'] = time.time()

            data['score'] = score+penalty_score
            if data['score']>agentmanagercommon.agentmanager_worst_score:
                data['score']=agentmanagercommon.agentmanager_worst_score
            json_str = json.dumps(data, default=lambda obj: obj.__dict__, sort_keys=True)
            redisutil.redisutil.sortedsetZADD(score,ip)
            redisutil.redisutil.hashset(ip, json_str)
    pass

    def del_proxie(self,proxie):
        redisutil.redisutil.hashdel(proxie)
        redisutil.redisutil.sortedsetZREM(proxie)
    pass

    def get_proxie(self,proxie):
        return redisutil.redisutil.hashget(proxie)
    pass

    def query_proxie(self,proxie):
        return redisutil.redisutil.hashget(proxie)
    pass

    def get_worst_proxie(self,proxie):
        return redisutil.redisutil.hashget(proxie)
    pass

    def use_updates_proxie(self,ip,is_success):
        redisob=redisutil.redisutil.hashget(ip)
        if redisob is None:
            agenttemp = agent_info(ip, 0, time.time(), time.time(), time.time(), 0, 0, 50)
            self.updataoradd_proxie(agenttemp)
        else :
            data = json.loads(redisob)
            if is_success==False:
                data['score'] =  data['score']+10
            else:
                data['last_success_time']=time.time()

            if data['score']>agentmanagercommon.agentmanager_worst_score:
                data['score']=agentmanagercommon.agentmanager_worst_score
            data['use_time'] = data['use_time']+1
            json_str = json.dumps(data, default=lambda obj: obj.__dict__, sort_keys=True)
            redisutil.redisutil.sortedsetZADD(data['score'],ip)
            redisutil.redisutil.hashset(ip, json_str)
    pass

    def calculate_penalty_time(self,last_success_time):
        return ((time.time()-last_success_time)/agentmanagercommon.agentmanager_abandon_time)*agentmanagercommon.agentmanager_full_penalty_score
    pass
agentmanagerutil=agentmanagerutil()

# 主启动程序
if __name__=="__main__":
    sss=redisutil.redisutil.sortedsetZRANGEBYSCORE(0,110)
    print(agentmanagerutil.providing_quality_proxie())
    for s in sss:
        redisob=agentmanagerutil.get_proxie(s)
        data = json.loads(redisob)
        data['last_success_time'] = time.time()
        json_str = json.dumps(data, default=lambda obj: obj.__dict__, sort_keys=True)
        redisutil.redisutil.hashset(data['ip'], json_str)
        print(data)
