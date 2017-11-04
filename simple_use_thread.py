#coding=utf-8;

from time import sleep,ctime
# python3 中要加_ 引入该模块

import _thread
"""
    全局解释器锁 GIL 保证同时只能有一个线程运行
    1> 设置GIL、
    2>切换进一个线程中去执行
    3>执行操作：指定数量的字节码指令 或者 线程主动让出控制权，调用time.sleep(0)来执行
    4>吧线程设置回睡眠状态，切换出线程
    5>解锁GIL
    6>重复上述步骤


"""

# 1不适用线程的情况
# 函数1 睡眠2秒
def loop0():
    print ("start loop0 at:%s" % ctime());
    sleep(2);
    print ("end loop0 at:%s"% ctime());

# 函数2 睡眠4 秒
def loop1():
    print ("start loop1 at:%s"%ctime());
    sleep(4);
    print ("end loop1 at:%s"%ctime());

def main():
    loop0();
    loop1();

"""
    程序执行完毕，用时6秒，这是两个单独的函数，所以我们需要多线程

"""

#
# if __name__ == "__main__":
#
#     main();

"""
    Python 中有多个模块支持多线程
    1> thread 不推荐使用 有缺点
    2> threading  提供更高级别 功能更加全面的线程管理
    3> Queue
    等 模块，

"""

# 2 thread 模块
"""
    核心函数  start_new_thread()
"""
def thread1():
    print ("thread1 start at:%s" % ctime());
    # 需要传递两个参数 一个函数名 一个函数的参数，即使不需要,也要传递一个空元组
    _thread.start_new_thread(loop0,());
    _thread.start_new_thread(loop1,());
    # 此处之所以睡眠6秒的原因 ，如果主线程代码继续执行的话，loop0 和 loop1 所在的线程直接会被终止，所以要进行等待
    sleep(6);

# 加锁



if __name__ =="__main__":
    thread1();
