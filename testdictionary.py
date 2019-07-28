# 测试字典
xiaoming = {"name": "小明", "age": 19, "height": 75}
print(xiaoming)

# 1.取值
print(xiaoming["name"])
# 修改
xiaoming["email"]="xiaoming@qq.com"
print(xiaoming)
# 2.增改

# 3.删除
xiaoming.pop("name")
print(xiaoming)

temp = {"address":"beijing"}

xiaoming.update(temp)
print(xiaoming)

xiaoming.clear()
print(xiaoming)