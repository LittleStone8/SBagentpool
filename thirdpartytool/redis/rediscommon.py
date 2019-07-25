# coding:utf-8
import configparser
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("SBagentpool\\")+len("SBagentpool\\")]  # 获取myProject，也就是项目的根路径
conf = configparser.ConfigParser()
conf.read(rootPath+'\\cofig.ini')


class RedisCommon:
    def __init__(self):
        self.host = conf.get('redis', 'host')
        self.password = conf.get('redis', 'password')
        self.port = conf.getint('redis', 'port')
        self.db = conf.getint('redis', 'db')

    pass


rediscommonObject=RedisCommon()
redis_link_host = rediscommonObject.host
redis_link_password = rediscommonObject.password
redis_link_port = rediscommonObject.port
redis_link_db =rediscommonObject.db

agent_redis_queue_key='SBagentpool_queue'

agent_redis_sortedset_key='SBagentpool_sortedset'

agent_redis_hash_key='SBagentpool_hash'



