from multiprocessing import Pool
import os, time, random

def woker(msg):
    t_start = time.time()
    print("%s 开始执行，进程号为 %d " % (msg, os.getpgid()))
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print("%s 执行完毕，耗时 %0.2f " % (t_stop - t_start))


def main():
    # 定义一个进程池，最大进程数3
    po = Pool(3)
    for i in range(0, 10):
        po.apply_async(woker, (i,))

    print("----start----")
    po.close()
    po.join()
    print("-----end----")


if __name__ == '__main__':
    main()