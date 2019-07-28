# 演示多线程
import threading
import time

def sayEat():
    print("吃饭啦")
    time.sleep(1)

def main():
    t1 = threading.Thread(sayEat())
    t2 = threading.Thread(sayEat())
    # 查看线程的数量

    t1.start()
    t2.start()
    while True:
        print(threading.enumerate())
        if len(threading.enumerate()) <=1:
            break
        time.sleep(1)

if __name__ == '__main__':
    main()

