def input_pasword():

    pwd = input("请输入密码:")

    if len(pwd) >= 8 :
        return pwd;

    print("主动抛出异常")

    ex = Exception("密码长度不够")

    raise ex

print(input_pasword())