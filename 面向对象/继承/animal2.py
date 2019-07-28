class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")


class Dog(Animal):
    def bark(self):
        print("汪汪叫")


class xiaotianquan(Dog):
    def eat(self):
        print("我爱吃咸蛋")

    def bark(self):
        print("叫喊二郎神")

        # super()调用父类方法
        super().bark()

        print("$$$$$#$$$%%#%%%(%(")



xt = xiaotianquan()
xt.eat()
xt.drink()
xt.bark()