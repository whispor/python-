import _thread
import time

def fun1(name,delay):
    print("开始运行线程fun1：%s"%name)
    time.sleep(delay)
    print("线程fun1: %s 结束"%name)

def fun2(name,delay):
    print("开始运行线程fun2：%s"%name)
    time.sleep(delay)
    print("线程fun2: %s 结束"%name)


if __name__ == "__main__":
    print("开始运行")
    _thread.start_new_thread(fun1,("haha", 3))
    _thread.start_new_thread(fun2,("hoho", 3))
    time.sleep(7)
    print("所有线程结束！")