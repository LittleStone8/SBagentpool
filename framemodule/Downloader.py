# coding:utf-8


import requests


class Downloader(object):
    def download_by_father(self, url,headers,timeout):
        return self.doquest(url,headers,timeout,None)
    pass

    def download_by_father_useagent(self, url,headers,timeout,proxies):
        return self.doquest(url,headers,timeout,proxies)
    pass


    def download_by_myself(self, url):
        return

    def download_by_myself_useagent(self, url):
        return

    def doquest(self, url,headers,timeout,proxies):
        try:
            my_response = requests.get(url=url, proxies=proxies, headers=headers, timeout=timeout)
            statuscode = my_response.status_code
            if statuscode == 200:
                return my_response.text
            else:
                return None
        except:
            return None
    pass

