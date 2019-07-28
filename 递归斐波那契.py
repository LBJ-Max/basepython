# 斐波那契用py实现

def fibonacci(num):
    if num == 1:
        return num
    elif num == 2:
        return num
    else:
        return fibonacci(num - 2) + fibonacci(num - 1)
for i in range(1, 10):
    print(fibonacci(i))
