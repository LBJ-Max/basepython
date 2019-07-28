class A:
    def __init__(self):
        self.num = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d" % (self.num, self.__num2))

    def test2(self):
        self.__test()

class B:

    pass

b = A()
# 在外界不能直接访问私有属性或者方法
b.test2()