# -*- coding=utf-8 -*-
# @Time: 2023/3/25 10:33
# @AUTHOR: HUI
# @File: thread_test1.py
# @software: PyCharm
# 1
"""1
import threading


def test(x, y):
    for i in range(x, y):
        print(i)


thread1 = threading.Thread(name='t1', target=test, args=(1, 10))
thread2 = threading.Thread(name='t2', target=test, args=(11, 20))
thread1.start()  # 启动线程1
thread2.start()  # 启动线程2"""
# 2
"""import threading
class mythread(threading.Thread):
    def run(self):
       for i in range(1,10):
           print(i)
thread1 = mythread()
thread2 = mythread()
thread1.start()
thread2.start()"""
# 3.
"""import time
import threading


def test():
    time.sleep(10)
    for i in range(10):
        print(i)


thread1 = threading.Thread(target=test, daemon=True)
thread1.start()
print('主线程完成了')"""
# 4.
"""
import time
import threading


def test():
    time.sleep(5)
    for i in range(10):
        print(i)


thread1 = threading.Thread(target=test)
thread1.start()
thread1.join()
print('主线程完成了')"""
# 5
"""# from threading import Thread, Event
# import time
# 
# 
# def countdown(n, started_evt):
#     print('正在运行')
#     started_evt.set()
#     while n > 0:
#         print('时间', n)
#         n -= 1
#         time.sleep(2)
# 
# 
# started_evt = Event()
# print('开始倒计时')
# t = Thread(target=countdown, args=(10, started_evt))
# t.start()
# started_evt.wait()
# print('倒计时运行')
"""
# 6.
"""# import threading
# 
# 
# class mythread(threading.Thread):
#     def run(self):
#         global x  # 声明一个全局变量
#         lock.acquire()  # 上锁
#         x += 10
#         print('%s:%d' % (self.name, x))
#         lock.release()  # 解锁
# 
# 
# x = 0  # 设置全局变量初始值
# lock = threading.RLock()  # 创建可重入锁
# list1 = []
# for i in range(5):
#     list1.append(mythread())  # 创建五个线程，放到同一列表中
# for i in list1:
#     i.start()  # 开启列表线程
"""
import threading
import time

condtion = threading.Condition()
sheep = ['1件产品', '1件产品', '1件产品', '1件产品', '1件产品']


class Producer(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)
        pass

    def run(self):
        global condtion, sheep
        while True:
            time.sleep(0.1)
            condtion.acquire()
            if len(sheep) < 10:
                print(self.name + "生产了1件产品")
                sheep.append('1件产品')
                condtion.notifyAll()
                pass
            else:
                print("仓库满了，停止生产!")
                condtion.wait()
                pass
            condtion.release()
        pass

    pass


class Customer(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)
        pass

    def run(self):
        global condtion, sheep
        while True:
            time.sleep(0.1)
            condtion.acquire()
            if len(sheep) > 0:
                meat = sheep.pop()
                print(self.name + "购买了" + meat + "还剩" + str(len(sheep)) + "件")
                condtion.notifyAll()
                pass
            else:
                print("买光了，等待")
                condtion.wait()
                pass
            condtion.release()
        pass

    pass


if __name__ == "__main__":
    p1 = Producer("1号生产车间")
    p2 = Producer("2号生产车间")
    p3 = Producer("3号生产车间")
    p4 = Producer("4号生产车间")
    p5 = Producer("5号生产车间")
    p6 = Producer("6号生产车间")
    p1.start()
    p2.start()
    p4.start()
    p5.start()
    p6.start()
    c1 = Customer('小王')
    c2 = Customer('小李')
    c3 = Customer('小贾')
    c4 = Customer('小沈')
    c5 = Customer('小刘')
    c1.start()
    c2.start()
    c3.start()
    c4.start()
    c5.start()
