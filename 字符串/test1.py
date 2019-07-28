# 字符串
hello_str = "hello world"
# 1.判断符串是否以指定的字符串开始
print(hello_str.startswith("hello"))

# 2.判断字符串结尾
print(hello_str.endswith("world"))

# 3.查找指定的字符串,索引，index也可以
print(hello_str.find("wor"))
print(hello_str.find("agb")) # 找不到输出-1 ,index找不到会报错
print(hello_str.index("wor"))

# 4.替换字符串,replace会返回新的字符串，不会修改原来的字符串
new_str = hello_str.replace("hel", "you")
print(new_str)