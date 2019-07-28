# 计算0 到100的和
i=0
result = 0
while i<= 100:
    if i % 2 == 0:
        print(i)
        result+=i
    # 处理计数器
    i+=1

print(result)
