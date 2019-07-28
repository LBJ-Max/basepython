class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")

##### 给猫类增加属性，不推荐外部的这种形式
tom = Cat()
tom.name = "tom"
print(tom.name)