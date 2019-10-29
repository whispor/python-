from threading import Thread
import time

# num =10
# def test1():
#     global num
#     for i in range(3):
#         num += 1
#     print("执行test1函数num的值：", num)

# def test2():
#     print("执行test2函数的值：", num)

# if __name__ == "__main__":
#     t1 = Thread(target=test1)
#     t2 = Thread(target=test2)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print("线程结束!")


num = 0
def test1():
    global num
    for i in range(1000000):
        # time.sleep(1)
        num += 1
    print("执行test1函数num的值：", num)

def test2():
    global num
    for i in range(1000000):
        # time.sleep(1)
        num += 1
    print("执行test2函数的值：", num)

if __name__ == "__main__":
    t1 = Thread(target=test1)
    t2 = Thread(target=test2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("线程结束!")