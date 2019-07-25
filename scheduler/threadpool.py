# coding:utf-8
#
import queue
import threading
import time
import contextlib
import traceback

StopEvent = object()


class ThreadPool(object):

    def __init__(self, max_num):
        self.q = queue.Queue()  # 最多创建的线程数（线程池最大容量）
        self.max_num = max_num

        self.terminal = False  # 如果为True 终止所有线程，不在获取新任务
        self.generate_list = []  # 真实创建的线程列表
        self.free_list = []  # 空闲线程数量

    def run(self, func, args, callback=None):
        """
        线程池执行一个任务
        :param func: 任务函数
        :param args: 任务函数所需参数
        :param callback: 任务执行失败或成功后执行的回调函数，回调函数有两个参数1、任务函数执行状态；2、任务函数返回值（默认为None，即：不执行回调函数）
        :return: 如果线程池已经终止，则返回True否则None
        """

        if len(self.free_list) == 0 and len(self.generate_list) < self.max_num:
            self.generate_thread()  # 创建线程
        w = (func, args, callback,)  # 把参数封装成元祖
        self.q.put(w)  # 添加到任务队列

    def generate_thread(self):
        """
        创建一个线程
        """
        t = threading.Thread(target=self.call)
        t.start()

    def call(self):
        """
        循环去获取任务函数并执行任务函数
        """
        current_thread = threading.currentThread  # 获取当前线程
        self.generate_list.append(current_thread)  # 添加到已经创建的线程里

        event = self.q.get()  # 取任务并执行
        while event != StopEvent:  # 是元组=》是任务；如果不为停止信号  执行任务

            func, arguments, callback = event  # 解开任务包； 分别取出值
            try:
                result = func(*arguments)  # 运行函数，把结果赋值给result
                status = True  # 运行结果是否正常
            except Exception as e:
                status = False  # 表示运行不正常
                result = e  # 结果为错误信息
                exstr = traceback.format_exc()
                print(e)
                print(exstr)

            if callback is not None:  # 是否存在回调函数
                try:
                    callback(status, result)  # 执行回调函数
                except Exception as e:
                    pass

            if self.terminal:  # 默认为False，如果调用terminal方法
                event = StopEvent  # 等于全局变量，表示停止信号
            else:
                # self.free_list.append(current_thread)  #执行完毕任务，添加到闲置列表
                # event = self.q.get()  #获取任务
                # self.free_list.remove(current_thread)  # 获取到任务之后，从闲置列表中删除；不是元组，就不是任务
                with self.worker_state(self.free_list, current_thread):
                    event = self.q.get()
            time.sleep(0.01) # 休息10毫秒
        else:
            self.generate_list.remove(current_thread)  # 如果收到终止信号，就从已经创建的线程列表中删除

    def close(self):  # 终止线程
        num = len(self.generate_list)  # 获取总共创建的线程数
        while num:
            self.q.put(StopEvent)  # 添加停止信号，有多少线程添加多少表示终止的信号
            num -= 1

    def terminate(self):  # 终止线程（清空队列）

        self.terminal = True  # 把默认的False更改成True

        while self.generate_list:  # 如果有已经创建线程存活
            self.q.put(StopEvent)  # 有几个线程就发几个终止信号
        self.q.empty()  # 清空队列

    @contextlib.contextmanager
    def worker_state(self, state_list, worker_thread):
        state_list.append(worker_thread)
        try:
            yield
        finally:
            state_list.remove(worker_thread)
