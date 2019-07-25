from agentpool.agentcraw.xiciagent import xicicommon
from agentpool.agentcraw.xiciagent.xiciUrlmanager import xiciUrlmanager
from agentpool.agentcraw.xiciagent.xicidownloader import xicidownloader
from agentpool.agentcraw.xiciagent.xicioutputer import xicioutputer
from agentpool.agentcraw.xiciagent.xiciparser import xiciparser
from common import agentsrc
from framemodule.Craw import Craw



class xiciCraw(Craw):
    def __init__(self,Scheduler):
        self.urlmanager = xiciUrlmanager()
        self.downloader = xicidownloader()
        self.parser = xiciparser()
        self.outputer = xicioutputer()
        self.job_interval= xicicommon.xici_craw_interval
        self.scheduler=Scheduler
        pass

    def docraw(self):
        self.start_craw()
        if self.job_interval!=0:
            self.scheduler.timer.addtask(self.start_craw,self.job_interval)
    pass

    def start_craw(self):
        print('启动开始抓取xici代理任务:')
        for url in self.urlmanager.new_urls:
            self.scheduler.run_in_main_threadpool(func=self.craw, args=(url,))
    pass

    def craw(self,url):
        print('开始抓取:'+url)
        html = self.downloader.download_by_myself_useagent(url)
        data = self.parser.parse(url, html)
        returndata = 0
        if data != None:
            returndata = str(len(data))
        print(url + "返回数据:" + str(returndata))
        storagesum=self.outputer.collect_data(data,url,agentsrc.xici)
        print(url + "抓取完毕,入库:"+str(storagesum))

