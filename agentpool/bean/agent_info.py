# coding=utf-8
import json
import time

import son as son
from redis import StrictRedis
class agent_info:
    def __init__(self,ip,port,recent_use_time,use_time,carw_time,carw_src,response_time,score=0,last_success_time=time.time()):
        self=self
        self.ip=ip
        self.port=port
        self.recent_use_time=recent_use_time
        self.use_time= use_time # 开
        self.carw_time = carw_time  # 开
        self.carw_src = carw_src  # 开
        self.response_time=response_time
        self.score=score
        self.last_success_time=last_success_time
    pass
