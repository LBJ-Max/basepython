# 列表的例子
name_list = ["张三", "李四", "王五"]
for name in name_list:
    print(name)

print(end="")
# 获取数据
print(name_list[0])

# 列表的操作
name_list[2]= "瓦格纳"
print(name_list)

# 列表尾部追加
name_list.append("sdff")

print(name_list)
# 插入数据，指定位置
name_list.insert(1, "xxxx")
print(name_list)
# extend操作合并列表
temp_list=["何珂沁", "周小璞"]
name_list.extend(temp_list)
print(name_list)

#从列表删除数据
name_list.pop(1)
print(name_list)

name_list.remove("李四")
print(name_list)

# name_list.clear()
print(name_list)

del name_list[1]
print(name_list)