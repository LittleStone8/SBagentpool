import time

from agentpool.agentcraw.zhandaye import zhandayecommon
from agentpool.agentcraw.zhandaye.zhandayedownloader import zhandayedownloader
from agentpool.agentcraw.zhandaye.zhandayeoutputer import zhandayeoutputer
from agentpool.agentcraw.zhandaye.zhandayeparser import zhandayeparser
from common import agentsrc
from framemodule.Craw import Craw


class zhandayeCraw(Craw):
    def __init__(self,Scheduler):
        self.downloader = zhandayedownloader()
        self.parser = zhandayeparser()
        self.outputer = zhandayeoutputer()
        self.job_interval= zhandayecommon.zhandaye_craw_interval
        self.scheduler=Scheduler
        pass

    def docraw(self):
        self.start_craw()
        if self.job_interval != 0:
            self.scheduler.timer.addtask(self.start_craw, self.job_interval)
    pass

    def start_craw(self):
        print('启动开始抓取zhandaye代理任务:')
        start_stage=int((time.time()-zhandayecommon.zhandaye_time_sign)/3600+zhandayecommon.zhandaye_stage_sign-zhandayecommon.zhandaye_stage_error)

        for stage in range(start_stage,start_stage+2*zhandayecommon.zhandaye_stage_error):
            url_zhandaye = zhandayecommon.zhandaye_url % (stage)
            self.scheduler.run_in_main_threadpool(func=self.craw, args=(url_zhandaye,))
    pass

    def craw(self,url):
        print('开始抓取:' + url)
        html = self.downloader.download_by_myself_useagent(url)
        data = self.parser.parse(url, html)
        returndata = 0
        if data != None:
            returndata = str(len(data))
        print(url + "返回数据:" + str(returndata))
        storagesum = self.outputer.collect_data(data, url, agentsrc.zhandaye)
        print(url + "抓取完毕,入库:" + str(storagesum))
    pass

