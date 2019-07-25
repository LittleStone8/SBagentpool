# coding:utf-8
import threading

import schedule
import time



class Timer:
    def __init__(self):
        self.is_open=True
        t = threading.Thread(target=self.call)
        t.start()
    pass

    def close(self):
        self.is_open=False
    pass

    def call(self):
        while self.is_open:
            schedule.run_pending()
            time.sleep(1)
    pass

    def addtask(self,func,interval):
        schedule.every(interval).seconds.do(func)




