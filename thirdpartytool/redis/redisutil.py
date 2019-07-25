# coding:utf-8
import json

import requests
from redis import StrictRedis

from thirdpartytool.redis import rediscommon


class RedisUtil:
    def __init__(self):
        self.redishanndle = StrictRedis(host=rediscommon.redis_link_host, port=rediscommon.redis_link_port,
                                        db=rediscommon.redis_link_db, password=rediscommon.redis_link_password)
    pass

    def queuelpush(self,json_str):
        self.redishanndle.lpush(rediscommon.agent_redis_queue_key, json_str)
    pass

    def queuelpop(self):
        return self.redishanndle.lpop(rediscommon.agent_redis_queue_key)
    pass

    def queuerpush(self,json_str):
        self.redishanndle.rpush(rediscommon.agent_redis_queue_key, json_str)
    pass

    def queuerpop(self):
        return self.redishanndle.rpop(rediscommon.agent_redis_queue_key)
    pass

    def hashset(self,field,value):
        self.redishanndle.hset(rediscommon.agent_redis_hash_key,field,value)
    pass

    def hashget(self,field):
        return self.redishanndle.hget(rediscommon.agent_redis_hash_key,field)
    pass

    def hashexists(self,field):
        return self.redishanndle.hexists(rediscommon.agent_redis_hash_key,field)
    pass

    def hashdel(self,field):
        return self.redishanndle.hdel(rediscommon.agent_redis_hash_key,field)
    pass

    def hashexistsprint(self):
        print (self.redishanndle.hkeys(rediscommon.agent_redis_hash_key))
    pass

    #向有序集合添加一个或多个成员，或者更新已存在成员的分数
    def sortedsetZADD(self,score,member):
        adddata = {member: score}
        self.redishanndle.zadd(rediscommon.agent_redis_sortedset_key,adddata)
    pass

    #获取有序集合的成员数
    def sortedsetZCARD(self):
        return self.redishanndle.zcard(rediscommon.agent_redis_sortedset_key)
    pass

    #移除有序集合中的一个或多个成员
    def sortedsetZREM(self,member):
        self.redishanndle.zrem(rediscommon.agent_redis_sortedset_key, member)
    pass

    #通过索引区间返回有序集合成指定区间内的成员
    def sortedsetZRANGE(self,start,stop):
        returndata=[]
        datalist=self.redishanndle.zrange(rediscommon.agent_redis_sortedset_key, start, stop)
        for data in datalist:
            returndata.append(str(data, 'utf-8'))
        return returndata
    pass

    #返回有序集合中指定成员的索引
    def sortedsetZRANK(self, member):
        return self.redishanndle.zrank(rediscommon.agent_redis_sortedset_key, member)
    pass

    #返回有序集中，成员的分数值
    def sortedsetZSCORE(self, member):
        return self.redishanndle.zscore(rediscommon.agent_redis_sortedset_key, member)
    pass
    #返回有序集中指定区间内的成员，通过索引，分数从高到底
    def sortedsetZREVRANGE (self, start,stop):
        returndata = []
        datalist=self.redishanndle.zrevrange(rediscommon.agent_redis_sortedset_key, start,stop)
        for data in datalist:
            returndata.append(str(data, 'utf-8'))
        return returndata
    pass
    #返回有序集中 最前面的第几个
    def sortedsetGETTOP (self, number):
        returndata=[]
        sum=self.redishanndle.zcard(rediscommon.agent_redis_sortedset_key)
        datalist = self.redishanndle.zrevrange(rediscommon.agent_redis_sortedset_key, sum - number, sum)
        for data in datalist:
            returndata.append(str(data, 'utf-8'))
        return returndata
    pass

    #按分数返回一个成员范围的有序集合。
    def sortedsetZRANGEBYSCORE (self, min,max,start=None, num=None,):
        returndata=[]
        datalist=self.redishanndle.zrangebyscore(rediscommon.agent_redis_sortedset_key,min,max,start,num)
        for data in datalist:
            returndata.append(str(data, 'utf-8'))
        return returndata
    pass

    #计算在有序集合中指定区间分数的成员数
    def sortedsetZCOUNT(self, min,max):
        return self.redishanndle.zcount(rediscommon.agent_redis_sortedset_key,min,max)
    pass

redisutil=RedisUtil()


# 主启动程序
if __name__=="__main__":
    redisUtil=RedisUtil();
    #redisUtil.hashexistsprint()
    #redisUtil.redishanndle.delete(rediscommon.agent_redis_hash_key)
    #redisUtil.hashexistsprint()
    #redisutil.redishanndle.zremrangebyscore(rediscommon.agent_redis_sortedset_key, 0, 1000)
    #print(redisUtil.hashexists('111.40.84.73:9999'))
    print(redisUtil.sortedsetZCARD())
    print(redisUtil.redishanndle.hlen(rediscommon.agent_redis_hash_key))
    #ss=redisUtil.sortedsetZRANGEBYSCORE(76, 9999)
    #print(len(ss))
    '''''
    for s in ss:
        aa = redisUtil.hashget(s)
        bb = json.loads(aa)
        bb['score']=75
        json_str = json.dumps(bb, default=lambda obj: obj.__dict__, sort_keys=True)
        #print(bb['ip']+':'+json_str)
        redisutil.hashset(bb['ip'], json_str)
    #hash_key = bb['ip']

    #redisutil.hashset(hash_key, json_str)

    print(len(ss))
    #redisUtil.sortedsetZRANGEBYSCORE(90, 9999)
    
    print(redisUtil.redishanndle.zrevrange(rediscommon.agent_redis_sortedset_key, 0, 10))
    aa=redisUtil.hashget('49.72.134.116:9999')
    print(aa)
    aa = redisUtil.hashget('49.51.70.42:1080')
    print(aa)
    aa = redisUtil.hashget('49.51.68.122:1080')
    print(aa)
    aa = redisUtil.hashget('47.94.136.5:8118')
    print(aa)
    aa = redisUtil.hashget('47.93.18.195:80')
    print(aa)
    print('asdasdsa\nasdsada')
    print(redisUtil.sortedsetZCOUNT(100, 200))
    print(redisUtil.sortedsetZCOUNT(0,30))
    #redisUtil.hashexistsprint()
    aa=redisUtil.hashget('182.150.35.76:80')
    print(aa)
    bb = json.loads(aa)
    bb['carw_src'] = 5

    json_str = json.dumps(bb, default=lambda obj: obj.__dict__, sort_keys=True)
    hash_key = bb['ip']
    redisutil.hashset(hash_key, json_str)

    #redisUtil.redishanndle.delete(rediscommon.agent_redis_hash_key)
    #key='192.192.192.192:88'
    #score=4.23
    #a = {key: score}
    #redisUtil.sortedsetZADD(4.51,'88888')
    redisUtil.sortedsetZADD(4.51, '5')
    #edisUtil.sortedsetZADD("4.356","3.54")
    #redisUtil.redishanndle.zadd(rediscommon.agent_redis_sortedset_key, a)
    print(redisUtil.sortedsetZCARD())
    abc=redisUtil.sortedsetZRANGE(0, 222)
    print(abc)
    print(redisUtil.sortedsetZREVRANGE(redisUtil.sortedsetZCARD()-1,redisUtil.sortedsetZCARD()))
    print(redisUtil.sortedsetZRANGEBYSCORE(4.51,4.51))

    print(redisUtil.redishanndle.zrangebyscore(rediscommon.agent_redis_sortedset_key, 4.51, 4.51,2,2))

    #ww=redisUtil.sortedsetZSCORE('3222')
    #print(ww)
    #proxiesipstr = str(abc[0], 'utf-8')
    #print(proxiesipstr)
    #print(22)

    #print(redisUtil.redishanndle.llen(rediscommon.agent_redis_queue_key))

    #while True:
    #    proxiesip=redisUtil.queuelpop()
'''''


