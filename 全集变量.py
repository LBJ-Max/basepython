num = 10
def demo1():
    #希望修改全局变量---使用global声明变量即可
    global num

    num = 99

    print(num)


def demo2():
    print(num)
    

demo1()
demo2()