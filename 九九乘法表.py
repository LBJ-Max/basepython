# 使用循环打印99乘法表
# 1.打印9行星星
row =1
while row <= 9 :
    col = 1
    while col <= row:
        # print("*", end="")
        # \t转义字符   空格
        print("%d * %d = %d" %(row, col, row * col) , end="\t")
        col += 1
    # print("%d" % row)

    print("")
    row += 1