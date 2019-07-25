# coding:utf-8
from scheduler import schedulercommon

from scheduler.threadpool import ThreadPool
from scheduler.timer import Timer


class Scheduler:
    def __init__(self):
        self.main_threadpool=ThreadPool(schedulercommon.main_thread_pool_size)
        self.second_threadpool = ThreadPool(schedulercommon.second_thread_pool_size)
        self.third_threadpool = ThreadPool(schedulercommon.third_thread_pool_size)
        self.fourth_threadpool = ThreadPool(schedulercommon.fourth_thread_pool_size)
        self.agentmanager_threadpool = ThreadPool(schedulercommon.agentmanager_thread_pool_size)
        self.job_list=[];
        self.timer=Timer()
        self.timer.addtask(self.print_Scheduler_stuart, 60)
    pass

    def add_job(self,Myjob):
        self.job_list.append(Myjob)
        Myjob.do_job()
    pass

    def run_in_main_threadpool(self, func, args, callback=None):
        self.main_threadpool.run(func,args,callback)
    pass

    def run_in_second_threadpool(self, func, args, callback=None):
        self.second_threadpool.run(func,args,callback)
    pass

    def run_in_third_threadpool(self, func, args, callback=None):
        self.third_threadpool.run(func,args,callback)
    pass

    def run_in_fourth_threadpool(self, func, args, callback=None):
        self.fourth_threadpool.run(func,args,callback)
    pass

    def run_in_agentmanager_threadpool(self, func, args, callback=None):
        self.agentmanager_threadpool.run(func,args,callback)
    pass

    def addage(self):
        print(222)
    pass

    def print_Scheduler_stuart(self):

        prstr=str('*********Scheduler state*********\n'+
        'main_threadpool{generate_list:' + str(len(self.main_threadpool.generate_list))+
        '  free_list:' + str(len(self.main_threadpool.free_list))+
        '  task_queue:' + str(self.main_threadpool.q.qsize())+'\n'
        'second_threadpool{generate_list:' + str(len(self.second_threadpool.generate_list))+
        '  free_list:' + str(len(self.second_threadpool.free_list))+
        '  task_queue:' + str(self.second_threadpool.q.qsize())+'\n'
        'third_threadpool{generate_list:' + str(len(self.third_threadpool.generate_list))+
        '  free_list:' + str(len(self.third_threadpool.free_list))+
        '  task_queue:' + str(self.third_threadpool.q.qsize())+'\n'
        'fourth_threadpool{generate_list:' + str(len(self.fourth_threadpool.generate_list))+
        '  free_list:' + str(len(self.fourth_threadpool.free_list))+
        '  task_queue:' + str(self.fourth_threadpool.q.qsize())+'\n'
        'agentmanager_threadpool{generate_list:' + str(len(self.agentmanager_threadpool.generate_list))+
        '  free_list:' + str(len(self.agentmanager_threadpool.free_list))+
        '  task_queue:' + str(self.agentmanager_threadpool.q.qsize()))

        print(prstr)
        ''''
        print('*********Scheduler state*********'
              )
        print('main_threadpool{generate_list:'+str(len(self.main_threadpool.generate_list))
              +'  free_list:'+str(len(self.main_threadpool.free_list))
              +'  task_queue:'+str(self.main_threadpool.q.qsize())
              )
        print('second_threadpool{generate_list:'+str(len(self.second_threadpool.generate_list))
              +'  free_list:'+str(len(self.second_threadpool.free_list))
              +'  task_queue:'+str(self.second_threadpool.q.qsize())
              )
        print('third_threadpool{generate_list:'+str(len(self.third_threadpool.generate_list))
              +'  free_list:'+str(len(self.third_threadpool.free_list))
              +'  task_queue:'+str(self.third_threadpool.q.qsize())
              )
        print('fourth_threadpool{generate_list:'+str(len(self.fourth_threadpool.generate_list))
              +'  free_list:'+str(len(self.fourth_threadpool.free_list))
              +'  task_queue:'+str(self.fourth_threadpool.q.qsize())
              )
        print('agentmanager_threadpool{generate_list:'+str(len(self.agentmanager_threadpool.generate_list))
              +'  free_list:'+str(len(self.agentmanager_threadpool.free_list))
              +'  task_queue:'+str(self.agentmanager_threadpool.q.qsize())
              )
        '''''
    pass