# 创建互斥锁
import threading
import time

# 定义全局变量
g_num = 0

# 创建一个互斥锁，默认是没有锁的
mutex = threading.Lock()

def test1(num):
    # 如果之前没有上锁，那么上锁成功
    # 如果上了锁，那么就会阻塞
    mutex.acquire()
    print("test1我进入锁了")
    global g_num
    for i in range(num):
        g_num += 1
    mutex.release()
    print("======== in test1 g_num=%d=====" % g_num)

def test2(num):
    global g_num
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()
    print("======== in test1 g_num=%d=====" % g_num)



def main():
    t1 = threading.Thread(target=test1, args=(10,))
    t2 = threading.Thread(target=test2, args=(10,))
    t1.start()
    t2.start()

    time.sleep(2)


if __name__ == '__main__':
    main()