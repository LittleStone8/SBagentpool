# coding:utf-8
import configparser
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("SBagentpool\\")+len("SBagentpool\\")]  # 获取myProject，也就是项目的根路径
conf = configparser.ConfigParser()
conf.read(rootPath+'\\cofig.ini')

#站大爷
class zhandaye_common:
    def __init__(self):
        zhandaye_time_sign = conf.getint('zhandaye', 'zhandaye_time_sign')
        zhandaye_stage_sign = conf.getint('zhandaye', 'zhandaye_stage_sign')
        zhandaye_url = conf.get('zhandaye', 'zhandaye_url')
        zhandaye_stage_error = conf.getint('zhandaye', 'zhandaye_stage_error')
        zhandaye_craw_interval = conf.getint('zhandaye', 'zhandaye_craw_interval')

        self.zhandaye_time_sign = zhandaye_time_sign#时间标记
        self.zhandaye_stage_sign = zhandaye_stage_sign#页数标记
        self.zhandaye_url=zhandaye_url
        self.zhandaye_stage_error = zhandaye_stage_error
        self.zhandaye_craw_interval = zhandaye_craw_interval
    pass
zhandayecommonObject=zhandaye_common()
zhandaye_time_sign = zhandayecommonObject.zhandaye_time_sign # 初始化结构对象
zhandaye_stage_sign = zhandayecommonObject.zhandaye_stage_sign
zhandaye_url = zhandayecommonObject.zhandaye_url
zhandaye_stage_error=zhandayecommonObject.zhandaye_stage_error
zhandaye_craw_interval=zhandayecommonObject.zhandaye_craw_interval