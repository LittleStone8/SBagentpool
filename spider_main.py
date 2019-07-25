
# 主启动程序
from agentpool.agentcraw.seleniumer.seleniumerCraw import seleniumerCraw
from agentpool.agentcraw.xiciagent.xiciCraw import xiciCraw
from agentpool.agentcraw.zhandaye.zhandayeCraw import zhandayeCraw
from agentpool.agentmanager.agentmanager import agentmanager
from scheduler.myscheduler import Scheduler

if __name__=="__main__":
    scheduler = Scheduler()
    print(222)
    #启动管理池`
    agentmanager=agentmanager(scheduler)
    scheduler.add_job(agentmanager)
    #启动xicicraw
    xicicraw = xiciCraw(scheduler)
    scheduler.add_job(xicicraw)
    #启动selenium框架craw
    seleniumer = seleniumerCraw(scheduler)
    scheduler.add_job(seleniumer)
    # 启动站大爷craw
    zhandaye = zhandayeCraw(scheduler)
    scheduler.add_job(zhandaye)
