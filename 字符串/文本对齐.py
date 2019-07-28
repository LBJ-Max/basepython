# 测试文本对齐的例子 ljust rjust center
poem=["登鹳雀楼",
      "王之涣",
      "白日依山尽",
      "黄河入海流",
      "欲穷千里目",
      "更上一层楼"]

for poem_str in poem:
    #剧中对齐
    print("| %s |" % poem_str.rjust(10, " "))