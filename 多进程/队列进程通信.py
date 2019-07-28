# 使用queue队列通信
import multiprocessing

from multiprocessing import Queue

# 创建队列对象
q = Queue(3)
q.put("111")
q.put(2222)
q.put([11, 22, 33])
# 判断队列是否满
print(q.full())
print(q.empty())

# 获取数据
print(q.get())
print(q.get())
print(q.full())
print(q.get())
