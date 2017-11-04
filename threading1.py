#coding=utf-8;

import threading
from time import sleep ,ctime

"""
    threading 模块包含非常好用的同步机制

    支持守护线程：
    主线程准备退出的手，不需要等待某些子线程，直接退出。特定的子线程就是守护线程，证明是不重要的。
    给守护线程添加标记
    thread.daemon = True

"""
# 1 Thread 类
"""
    属性
    1> name  名字 2> ident 标识符  3> daemon 是否是守护线程
    对象方法

"""

loops= [2,4];

def loop(nloop,nsec):
    print ("start loop %s at %s"%(nloop,ctime()));
    sleep(nsec);
    print ("end loop %s at %s"%(nloop,ctime()));

def main():
    print ("starting at:",ctime());
    threads = [];
    nloops = range(len(loops));

    for i in nloops:
        # 创建线程
        t = threading.Thread(target=loop,args=(i,loops[i]))
        # 将线程装进数组中去
        threads.append(t);

    # 开启线程
    for i in nloops:
        threads[i].start();

    # 等待所有的线程结束
    for i in nloops:
        # join 函数，直至启动的线程终止之前一直挂起，除非给出特定的时间，否则一直阻塞
        # join 可以传递一个参数，timeout = "" 指定的超时时间
        threads[i].join();

    # 所有的完成
    print ("all jobs done %s",ctime());




# 创建一个Thread 的实例 传递一个可调用累的实例，这是更加趋向于面型对象的编程

class threadFunc():
    def __init__(self,funs,args,name=''):
        self.name = name;
        self.func =funs;
        self.args = args;

    def __call__(self):
        self.func(*self.args);
        print ("self.name == %s"%self.name);

def loop1(nloop,nsec):
    print ("start loop %s at %s"%(nloop,ctime()));
    sleep(nsec);
    print ("end loop %s at %s"%(nloop,ctime()));

def main1():
    print ("start job at %s",ctime());
    threads = [];
    nloops = range(len(loops));

    # 创建线程
    for i in  nloops:
        t = threading.Thread(target=threadFunc(loop1,(i,loops[i]),loop1.__name__));
        threads.append(t);

    # start
    for i in nloops:
        threads[i].start();

    # join
    for i in nloops:
        threads[i].join();

    print ("all jobs done %s", ctime());

if __name__ == "__main__":
    main1();