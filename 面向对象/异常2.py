# 提示用户输入一个整数
try:

    num = int(input("输入一个整数"))

    result = 8/num

    print(result)

except ZeroDivisionError:
    print("除0错误")

except ValueError:
    print("数值类型不匹配")