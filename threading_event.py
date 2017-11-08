#coding=utf-8;

import  threading
import time


"""
    Python 提供了Event对象用于线程通信，它是由线程设置的信号标志
    1 设置信号
    使用set方法 设置Event 对象内部的信号标志为真
    isSet 方法来判断方法是否返回真

    2 清除信号
    clear 方法可以清除event 对象内部的信号标志，将其设置为假

    3 等待
    wait方法，当event 信号标志为真的时候才会很快执行并且返回，当Event内部信号标志位为
    假的时候，wait方法一直等待其为真的时候才返回
"""

class Task(threading.Thread):
    def __init__(self,n):
        super(Task,self).__init__();
        self.name = "Thread --" + str(n);

    # run 函数
    def run(self):
        global event;
        # 第一次就让他清楚 让他等待
        if event.isSet():
            event.clear();
            event.wait();
            print ("%s"%self.name);
        else:
            print ("%s"%self.name);
            event.set();



if __name__ == '__main__':
    # 实例化一个event 对象
    event = threading.Event();
    # 设置为真
    event.set();
    # 开启线程
    threads = [];
    for i in  range(10):
        t = Task(i);
        t.start();
"""
    打印结果：
Thread --1
Thread --0
Thread --3
Thread --2
Thread --5
Thread --4
Thread --7
Thread --6
Thread --9
Thread --8
"""


