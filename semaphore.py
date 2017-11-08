
#coding=utf-8;

import threading
import time

"""
    信号量的使用，就是可以保证两个或者多个代码段能够并发调用

    信号量 是一个非负的整数，所有通过它的线程都会讲整数减一，当其为0的时候，所有其他的线程都为等待状态

"""

class Task(threading.Thread):
    # 任务函数
    def __init__(self,n):
        # 重构init
        super(Task,self).__init__();
        self.name = "Thread--"+ str(n);

    # 定义run 函数
    def run(self):
        """
        定义了5个位最大并发量
        semaphore 的计数器
        当调用acquire 的时候 +1
        当调用release 的时候 -1

        :return:
        """
        semaphore.acquire();
        print ("%s"%self.name);
        time.sleep(1);
        semaphore.release();



if __name__ == '__main__':
    # 只允许同时5个线程并发
    semaphore = threading.BoundedSemaphore(5);
    # 循环启动50个线程
    threads = [];
    for i in range(1 ,51):
        t = Task(i);
        threads.append(t);
        t.start();







