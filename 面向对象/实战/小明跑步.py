class Person:

    def __init__(self, name, weight):
        # self.属性=形参
        self.name = name
        self.weight= weight

    def __str__(self):
        return "我的名字叫 %s 体重是 %.2f 公斤"  %(self.name, self.weight)


    def run(self):
        # pass占位符空方法
        # pass
        print("%s 爱跑步，跑步锻炼身体" % self.name)
        self.weight -= 0.5

    def eat(self):
        # pass
        print("%s 是吃货，吃完这顿在减肥" % self.name)
        self.weight += 1

xiaoming = Person("小明", 83.5)
xiaoming.run()
xiaoming.eat()
print(xiaoming)