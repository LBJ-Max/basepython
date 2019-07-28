import multiprocessing
from multiprocessing import  Queue

def download_from_web(q):
    # 下载数据
    data = [11, 22, 33, 44]
    # 队列写入数据
    for temp in data:
        q.put(temp)

    print("-----数据已经完全存入队列中了")

def analysis_data(q):
    waiting_list_data = list()
    while True:
        data = q.get()
        waiting_list_data.append(data)
        if q.empty():
            break

    print("----开始分析数据数据列表为---")
    for temp in waiting_list_data:
        print(temp)

def main():
    # 1.创建队列
    q = Queue()
    p1 = multiprocessing.Process(target= download_from_web, args=(q,))
    p2 = multiprocessing.Process(target= analysis_data, args=(q,))

    p1.start()
    p2.start()

if __name__ == '__main__':
     main()