from agentpool.agentcraw.seleniumer import seleniumerCommon
from agentpool.agentcraw.seleniumer.seleniumerloader import Seleniumerloader
from agentpool.agentcraw.seleniumer.seleniumeroutputer import Seleniumeroutputer
from agentpool.agentcraw.seleniumer.seleniumerurlmanager import SeleniumerUrlmanager
from common import agentsrc
from framemodule.Craw import Craw


class seleniumerCraw(Craw):
    def __init__(self,Scheduler):
        self.urlmanager = SeleniumerUrlmanager()
        self.downloader = Seleniumerloader()
        self.outputer = Seleniumeroutputer()
        self.job_66_craw_interval = seleniumerCommon.seleniumer_url_66_craw_interval
        self.job_kuaidaili_craw_interval = seleniumerCommon.seleniumer_url_kuaidaili_craw_interval
        self.scheduler=Scheduler
        pass

    def docraw(self):
        self.start_kuaidailicraw()
        if self.job_kuaidaili_craw_interval != 0:
            self.scheduler.timer.addtask(self.start_kuaidailicraw, self.job_kuaidaili_craw_interval)
        self.start_66craw()
        if self.job_66_craw_interval != 0:
            self.scheduler.timer.addtask(self.start_66craw, self.job_66_craw_interval)
    pass

    def start_kuaidailicraw(self):
        print('启动开始抓取快代理任务:')
        new_urls_kuaidaili = self.urlmanager.get_new_url_kuaidaili()
        url_xpath_kuaidaili = self.urlmanager.url_xpath_kuaidaili
        if len(new_urls_kuaidaili) == 0:
            return
        for url in new_urls_kuaidaili:
            self.scheduler.run_in_second_threadpool(func=self.craw, args=(url, url_xpath_kuaidaili,agentsrc.kuaidaili))

    pass

    def start_66craw(self):
        print('启动开始抓取66代理任务:')
        new_urls_66 = self.urlmanager.get_new_url_66()
        url_xpath_66 = self.urlmanager.url_xpath_66
        if len(new_urls_66) == 0:
            return
        for url in new_urls_66:
            self.scheduler.run_in_second_threadpool(func=self.craw, args=(url, url_xpath_66,agentsrc.ip66,))

    pass

    def craw(self,url,url_xpath,angentsrc):
        print('开始抓取:' + url)
        data = self.downloader.download_by_myself_useagent(url,url_xpath)
        returndata=0
        if data!=None:
            returndata=str(len(data))
        print(url + "返回数据:"+str(returndata))
        storagesum=self.outputer.collect_data(data,url,angentsrc)
        print(url + "抓取完毕,入库:"+str(storagesum))

