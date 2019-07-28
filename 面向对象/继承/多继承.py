class A:
    def say(self):
        print("hello a")

class B:
    def sayb(self):
        print("hello b")

class C(A, B):
    pass

c = C()
c.say()
c.sayb()

# 确定c类方法搜索顺序
print(C.mro())