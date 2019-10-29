import time
from threading import Thread,Lock

num = 0
# 创建互斥锁
lock = Lock()
# def test1():
#     global num
#     # 上锁
#     lock.acquire()   
#     for i in range(1000000):
#         # time.sleep(1)
#         num += 1
#     # 释放锁
#     lock.release()
#     print("执行test1函数num的值：", num)

# def test2():
#     global num
#     lock.acquire()
#     for i in range(1000000):
#         # time.sleep(1)
#         num += 1
#     lock.release()
#     print("执行test2函数的值：", num)


def test1():
    global num
    for i in range(1000000):
        # time.sleep(1)
        # 上锁
        lock.acquire()   
        num += 1
        # 释放锁
        lock.release()
    print("执行test1函数num的值：", num)

def test2():
    global num
    for i in range(1000000):
        # time.sleep(1)
        lock.acquire()
        num += 1
        lock.release()
    print("执行test2函数的值：", num)



if __name__ == "__main__":
    t1 = Thread(target=test1)
    t2 = Thread(target=test2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("线程结束!")