# 提示用户输入一个整数
try:

    num = int(input("输入一个整数"))

    result = 8/num

    print(result)

except ZeroDivisionError:
    print("除0错误")


except Exception as result:
    print(result)

else :
    print("代码成功被执行")
finally:
    print("无论是否有错，都会执行")