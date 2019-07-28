# 对象初始化内置方法init ，定义类指定类包含哪些属性
class Cat:
    def __init__(self, new_name):
        print("初始化🐱类的初始化方法")

        # self.属性名 = 属性初始值
        self.name = new_name

    def eat(self):
        print("%s 爱吃鱼" % self.name)

# 使用类名创建对象时候，会自动调用初始化方法init_
tom = Cat("jerry")
print(tom.name)
tom.eat()