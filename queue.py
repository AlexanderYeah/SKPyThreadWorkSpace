#coding=utf-8;

import queue
import threading
import time
"""
    Python 的queue 模块 提供了同步的 线程安全的队列类 FIFO 队列Queue
    LIFO 队列 LifoQueue
    PriorityQueue 优先级队列
    这些队列都属于 锁原语

    对象方法：
    qsize（） 返回队列的大小
    empty（） 如果队列为空 则返回True
    full（） 如果队列满了 返回True
    put(item，block=True，timeout = None) 将 item放入队列
    get（）从队列取出元素
    task_done() 在完成一项工作之后 ，向已经完成的队列发送一个信号
    join（）


    Queue 就是提供线程之间的通信机制


    生产者 -- 消费者模型

    一个线程放入数据，就是生产者
    其他线程去使用这些数据，就是消费者

    生产者和消费者独立地且并发的执行线程

"""

# 退出标志
exitFlag = 0;

class myThread(threading.Thread):
    def __init__(self,ThreadID,name,q):
        threading.Thread.__init__(self);
        self.threadID = ThreadID;
        self.name = name;
        self.q = q;

    def run(self):
        print ("开启线程:%s--time%s"% (self.name,time.time()));
        process_data(self.name,self.q);
        print("退出线程:%s--time%s"% (self.name,time.time()));


def process_data(threadName,q):
    while not exitFlag:
        # 此条线程加锁做操作
        queueLock.acquire();
        if not workQueue.empty():
            # 取出先进的队列
            data = q.get();
            # 释放锁
            queueLock.release();
            print ("%s processing %s--time:%s" %(threadName,data,time.time()));
        else:
            queueLock.release();
        time.sleep(1);



threadList = ["Thread-1","Thread-2","Thread-3"];
nameList = ["One","Two","Three","Four","Five"];

# 实例化一个锁，此时的锁处于打开状态
queueLock= threading.Lock();
# 创建一个FIFO 队列，最大为10个item
workQueue = queue.Queue(10);
threads = [];
threadID = 1;

# 循环创建线程
for tName in threadList:
    thread =  myThread(threadID,tName,workQueue);
    thread.start();
    threads.append(thread);
    threadID += 1;
# 填充队列
queueLock.acquire();
for word in nameList:
    workQueue.put(word);
queueLock.release();


# 等待队列清空队列
while not workQueue.empty():
    pass;

# 通知线程是时候退出了
exitFlag = 1;

# 等待所有的线程完成
for  t in threads:
    t.join();
print ("退出主线程");






