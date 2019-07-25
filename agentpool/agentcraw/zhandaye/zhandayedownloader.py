# coding:utf-8
import json
import random
import time

import requests

from agentpool.agentcraw.xiciagent import xicicommon
from agentpool.agentmanager import agentmanagerutil, agentmanagercommon
from common.httpheader import getheaders
from framemodule.Downloader import Downloader


class zhandayedownloader(Downloader):
    def download_by_myself(self, url):
        agentmanagercommon.agentmanager_requestsum = agentmanagercommon.agentmanager_requestsum + 1
        agentmanagercommon.agentmanager_use_myself_time = agentmanagercommon.agentmanager_use_myself_time + 1
        headers = getheaders(1)  # 定制请求头
        return self.download_by_father(url, headers, xicicommon.xici_max_quest_timeout)
    pass

    def download_by_myself_useagent(self, url):
        proxiesips=agentmanagerutil.agentmanagerutil.providing_quality_proxie()
        for proxiesipstr in proxiesips:
            if proxiesips ==None:
                continue
            else:
                headers = getheaders(1)  # 定制请求头
                proxies = {"http": "http://" + proxiesipstr, "https": "http://" + proxiesipstr}  # 代理ip
                agentmanagercommon.agentmanager_requestsum = agentmanagercommon.agentmanager_requestsum + 1
                agentmanagercommon.agentmanager_use_proxy_time = agentmanagercommon.agentmanager_use_proxy_time + 1
                response = self.download_by_father_useagent(url, headers, xicicommon.xici_max_quest_timeout, proxies)
                if response is None:
                    agentmanagerutil.agentmanagerutil.use_updates_proxie(proxiesipstr,False)
                else:
                    agentmanagerutil.agentmanagerutil.use_updates_proxie(proxiesipstr,True)
                    agentmanagercommon.agentmanager_use_proxy_success_time = agentmanagercommon.agentmanager_use_proxy_success_time + 1
                    return response
            time.sleep(0.1)
        return self.download_by_myself(url)
    pass


