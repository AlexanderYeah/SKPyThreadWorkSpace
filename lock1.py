#coding=utf-8;

import threading
import time
"""
    线程锁是为了解决多个线程访问同一个数据的时候安全问题
    对于需要锁定的代码需要放在 acquire()  和  release() 方法之间
"""

# 定义一个全局变量
num = 0;
# 实例化一个锁，此时的锁处于打开状态
lock = threading.Lock();

class Task(threading.Thread):
    # 实现__init__
    def __init__(self,n):
        # 重构__init__,先执行父类的函数
        super(Task,self).__init__();
        self.name = "the thread-"+ str(n);

    # 任务函数 只能以run 命名
    def run(self):
        # 引用外部的全局变量
        global num;
        time.sleep(0.5);
        # 获取lock 加锁 数据n 的操作只能在此线程中进行
        if lock.acquire():
            num += 1;
            print("%s--n=%s"%(self.name,num));
            time.sleep(0.2);
            # 解锁操作 其他线程可以访问数据
            lock.release();


if __name__ == '__main__':
    # 数据 存储线程
    threads = [];
    for i in range(1,51):
        # 启动50个线程
        t = Task(i);
        threads.append(t);
        t.start();
    #等待所有线程结束 join 方法
    # time()方法返回的是浮点数
    # ctime() 方法返回的是时间戳字符串 str类型的
    start_time = time.time();
    for item in threads:
        item.join();


# 获取程序运行时间 一共时间 50*02 + 0.5
print("run time:%s",time.time() - start_time);


