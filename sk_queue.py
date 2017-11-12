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



    异常：
    Empty ：对空队列 调用get 方法 就会报异常
    Full：： 对已经满的队列 调用put 方法 也会报异常


    Queue 就是提供线程之间的通信机制


    生产者 -- 消费者模型

    一个线程放入数据，就是生产者
    其他线程去使用这些数据，就是消费者

    生产者和消费者独立地且并发的执行线程

"""




"""
    最为坑爹的是 刚开始此文件命名为 queue.py
    然后一直运行 一直失败，'module' has no attribute 'Queue" 的错误
    到最后才发现,原来是queue.py 和python 内置的queue 冲突。所以总是报错

    将文件名改完之后 ，一切OK了

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
        print ("开启线程:%s--time%s"% (self.name,time.ctime()));
        process_data(self.name,self.q);
        print("退出线程:%s--time%s"% (self.name,time.ctime()));

# 处理数据的函数
def process_data(threadName,q):
    while not exitFlag:
        # 此条线程加锁做操作
        queueLock.acquire();
        if not workqueue.empty():
            # 取出所谓生产者线程中的第一个数据
            data = q.get();
            # 释放锁
            queueLock.release();
            print ("%s processing %s--time:%s" %(threadName,data,time.ctime()));
        else:
            queueLock.release();
        time.sleep(1);



threadList = ["Thread-1","Thread-2","Thread-3"];
nameList = ["One","Two","Three","Four","Five"];



# 实例化一个锁，此时的锁处于打开状态
queueLock = threading.Lock()
# 创建一个FIFO 队列，最大可以存放10个item
workqueue = queue.Queue(10)
threads = [];
threadID = 1;

# 循环创建线程 并且开启线程
"""
    此处线程1，2，3是并发执行的
"""
for tName in threadList:
    thread =  myThread(threadID,tName,workqueue);
    thread.start();
    threads.append(thread);
    threadID += 1;

# 加锁此条线程 并且向队列中添加数据
queueLock.acquire();
for word in nameList:
    workqueue.put(word);
queueLock.release();


# 等待队列清空队列，队列如果不清空 则 exitFlag 仍为0 ，程序继续运行
# 一直在while 语句中循环
while not workqueue.empty():
    pass;

# 通知线程是时候退出了
exitFlag = 1;

# 等待所有的线程完成
for t in threads:
    t.join();

# 所有线程执行完毕 退出
print ("退出主线程");

"""
    打印结果：

开启线程:Thread-1--timeSun Nov 12 13:43:16 2017
开启线程:Thread-2--timeSun Nov 12 13:43:16 2017
开启线程:Thread-3--timeSun Nov 12 13:43:16 2017
Thread-3 processing One--time:Sun Nov 12 13:43:17 2017
Thread-1 processing Two--time:Sun Nov 12 13:43:17 2017
Thread-2 processing Three--time:Sun Nov 12 13:43:17 2017
Thread-3 processing Four--time:Sun Nov 12 13:43:18 2017
Thread-1 processing Five--time:Sun Nov 12 13:43:18 2017
退出线程:Thread-2--timeSun Nov 12 13:43:18 2017
退出线程:Thread-3--timeSun Nov 12 13:43:19 2017
退出线程:Thread-1--timeSun Nov 12 13:43:19 2017
退出主线程

"""




