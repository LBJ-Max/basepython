class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s 来了" % self.name)

    # 对象被销毁前调用系统自动调用
    def __del__(self):
        print("%s 我去了" % self.name)

    def __str__(self):
        # 必须返回一个字符串
        return "我是小猫[%s]" % self.name

tom =  Cat("tom")
print(tom)