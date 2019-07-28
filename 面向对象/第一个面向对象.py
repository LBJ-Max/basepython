class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")

# 创建猫对象
tom = Cat()
tom.drink()
tom.eat()
addr = id(tom)
print(addr)
print(tom)
print("%x" % addr)
