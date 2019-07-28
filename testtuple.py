# 元组使用
my_tuple = ("李明", 123, 23.3)
print(type(my_tuple))
print(my_tuple[0])
# 取值
print(my_tuple[0])
print(my_tuple.index(123))
print(my_tuple.count(123))
print(len(my_tuple))

# 遍历元组
for node in my_tuple:
    print(node)

# 元组转换为列表
num_list={1,3,4,5}
numbers = tuple(num_list)
print(type(numbers))


nums = list(my_tuple)
print(type(nums))
