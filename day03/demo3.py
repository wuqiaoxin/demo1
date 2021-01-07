#循环结构
# while 循环  条件型
# for循环   次数型
# for 变量 in range(0,10) 后面是范围
# *
# **
# ***
# ****

# for i in range(0,10):
#     print("*")

# for i in range(0,5):
#     for j in range(0,i+1):
#         print("*",end="")
#     print("")
num=int(input("请输入乘法表的层数："))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,"x",i,"=",(i*j),"\t",end="")
    print()


