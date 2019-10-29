import threading
import time

def fun1(name,delay):
    print("线程{}开始运行fun1".format(name))
    print("线程%s运行fun1：开始等待！"%name)
    time.sleep(delay)
    print("线程%s运行fun1：等待结束！"%name)
    print("线程{}运行fun1结束".format(name))

def fun2(name,delay):
    print("线程{}开始运行fun2".format(name))
    print("线程%s运行fun2：开始等待！"%name)
    time.sleep(delay)
    print("线程%s运行fun2：等待结束！"%name)
    print("线程{}运行fun2结束".format(name))

if __name__ == "__main__":
    print("开始运行")
    t1 = threading.Thread(target=fun1,args=("haha", 4))
    t2 = threading.Thread(target=fun2, args=("jojo", 4))
    t1.start()
    t2.start()
    t1.join()
    t2.join()