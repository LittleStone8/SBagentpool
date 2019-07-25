from framemodule.Downloader import Downloader
from framemodule.MyJob import MyJob
from framemodule.Outputer import Outputer
from framemodule.Parser import Parser
from framemodule.UrlManager import UrlManager


class Craw(MyJob):
    def __init__(self,Scheduler):
        self.urlmanager = UrlManager()
        self.downloader = Downloader()
        self.parser = Parser()
        self.outputer = Outputer()
        self.scheduler=Scheduler
        pass

    def do_job(self):
        self.docraw()
        pass

    def docraw(self):
        print('craw craw craw')
        pass
