import math
import queue

import requests

from common.httpheader import getheaders


def checkip(  ip):
    proxies = {"http": "http://" + ip, "https": "http://" + ip}  # 代理ip
    try:
        response = requests.get(url='https://www.baidu.com/', proxies=proxies, headers=getheaders(),
                                timeout=5).status_code
        if response == 200:
            return True
        else:
            return False
    except:
        return False
pass

#print(checkip('182.88.119.201:9797'))

#print(math.ceil(450/50))

q = queue.Queue()  # 最多创建的线程数（线程池最大容量）

print(q.qsize())