# 静态方法
class B(object):

    # 定义静态方法
    @staticmethod
    def talk():
        print("静态方法")

b = B()
b.talk()