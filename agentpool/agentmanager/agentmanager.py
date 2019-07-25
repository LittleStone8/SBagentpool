# coding=utf-8
import json
import math
import threading
import time

import requests
import schedule

from agentpool.agentmanager import agentmanagercommon, agentmanagerutil
from common.httpheader import getheaders
from framemodule.MyJob import MyJob
from scheduler.myscheduler import Scheduler
from thirdpartytool.redis import redisutil


class agentmanager(MyJob):
    def __init__(self,Scheduler):
        self.scheduler=Scheduler
        self.worst_cleaninglock=threading.RLock()
        self.worst_proxie_count_start = 0
        self.worst_proxie_count_end = 0
        self.worst_proxie_last_time = time.time()

        self.routine_proxie_count_start = 0
        self.routine_proxie_count_end = 0
        self.routine_proxie_last_time = time.time()
        self.routine_cleaninglock = threading.RLock()

        schedule.every(15).seconds.do(self.print_agentmanager_stuart)
    pass

    def do_job(self,):
        self.scheduler.run_in_agentmanager_threadpool(self.routine_cleaning,args=())
        self.scheduler.run_in_agentmanager_threadpool(self.worst_cleaning, args=())
        self.scheduler.run_in_agentmanager_threadpool(self.cleaning_dead, args=())
        pass

    # 常规清理
    def routine_cleaning(self):
        while True:
            thistime = time.time()
            interval=thistime-self.routine_proxie_last_time
            if self.routine_proxie_count_start == self.routine_proxie_count_end and interval>300:
                print('启动新一轮常规清理,据上一次清理时间为:' + str(int(thistime)))
                self.routine_proxie_last_time = thistime

                self.routine_proxie_count_start = 0

                start_score=0
                end_score=agentmanagercommon.agentmanager_worst_score-30.0001
                routineproxiesum = redisutil.redisutil.sortedsetZCOUNT(start_score, end_score)
                blocknunber = math.ceil(routineproxiesum / agentmanagercommon.agentmanager_routine_block)  # 向上取整
                self.routine_proxie_count_end = blocknunber
                for num in range(0, blocknunber):
                    start_inde=num * agentmanagercommon.agentmanager_routine_block
                    chenckproxies = redisutil.redisutil.sortedsetZRANGEBYSCORE(start_score,end_score, start_inde,agentmanagercommon.agentmanager_routine_block)
                    self.scheduler.run_in_third_threadpool(self.checkip, args=(chenckproxies,),
                                                           callback=self.routine_cleaning_caback)
            time.sleep(1)
    pass

    # 最坏清理
    def worst_cleaning(self):
        while True:
            thistime = time.time()
            interval = int(thistime - self.worst_proxie_last_time)
            if self.worst_proxie_count_start==self.worst_proxie_count_end and interval>300:
                print('启动新一轮最坏清理,据上一次清理时间为:' + str(interval))
                self.worst_proxie_last_time = thistime

                self.worst_proxie_count_start = 0
                start_score=agentmanagercommon.agentmanager_worst_score-30
                end_score=agentmanagercommon.agentmanager_worst_score
                worstproxiesum = redisutil.redisutil.sortedsetZCOUNT(start_score, end_score)
                blocknunber = math.ceil(worstproxiesum / agentmanagercommon.agentmanager_worst_block)  # 向上取整
                self.worst_proxie_count_end=blocknunber
                for num in range(0, blocknunber):
                    start_index=num*agentmanagercommon.agentmanager_worst_block
                    chenckproxies = redisutil.redisutil.sortedsetZRANGEBYSCORE(start_score,end_score,start_index,agentmanagercommon.agentmanager_worst_block)
                    self.scheduler.run_in_fourth_threadpool(self.checkip, args=(chenckproxies,),
                                                           callback=self.worst_cleaning_caback)
            time.sleep(1)
    pass

    # 清除满分代理
    def cleaning_dead(self):
        while True:
            deadproxies = redisutil.redisutil.sortedsetZRANGEBYSCORE(agentmanagercommon.agentmanager_worst_block, 9999)
            for deadproxie in deadproxies:
                redisutil.redisutil.sortedsetZREM(deadproxie)
                redisutil.redisutil.queuelpush(deadproxie)
            time.sleep(60)
    pass

    def worst_cleaning_caback(self,status, result):
        self.worst_cleaninglock.acquire()
        try:
            self.worst_proxie_count_start=self.worst_proxie_count_start+1
        finally:
            self.worst_cleaninglock.release()
    pass

    def routine_cleaning_caback(self,status, result):
        self.routine_cleaninglock.acquire()
        try:
            self.routine_proxie_count_start=self.routine_proxie_count_start+1
        finally:
            self.routine_cleaninglock.release()
    pass

    def print_agentmanager_stuart(self):
        prstr = str('*********Agentmanager state*********\n' +
                    '  requestsum:' + str(agentmanagercommon.agentmanager_requestsum) +
                    '  use_myself_time:' + str(agentmanagercommon.agentmanager_use_myself_time) +
                    '  use_proxy_time:' + str(agentmanagercommon.agentmanager_use_proxy_time) +
                    '  use_proxy_success_time:' + str(agentmanagercommon.agentmanager_use_proxy_success_time))
        print(prstr)
    pass

    def checkip(self,proxies):
        for proxie in proxies:
            proxies = {"http": "http://" + proxie, "https": "http://" + proxie}  # 代理ip
            score=0.0
            issuccess=False
            for chenckurl in agentmanagercommon.agentmanager_checkurls:
                headers = getheaders()  # 定制请求头
                starttime = time.time()
                try:
                    response=requests.get(url=chenckurl, proxies=proxies, headers=headers, timeout=agentmanagercommon.agentmanager_checkip_max_timeout).status_code
                    endtime = time.time()
                    if response == 200 :
                        score=score+(endtime-starttime)
                        issuccess=True
                    else:
                        score=score+agentmanagercommon.agentmanager_error_quest_score
                except:
                    score=score+agentmanagercommon.agentmanager_error_quest_score
                #更新代理
            agentmanagerutil.agentmanagerutil.updataoradd_proxiestr(proxie,score,issuccess)
    pass
if __name__=="__main__":
    scheduler=Scheduler()
    scheduler = agentmanager(scheduler)
    scheduler.do_job()

