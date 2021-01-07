# def sum(a,b):
#     s=a+b
#     return s
#
# a=12
# b=14
# print(sum(a,b))
# print(sum(1,4))
# 定义方法，传入一个n，打印NxN的乘法表。具有功能单一性。不要讲一个方法即可一个功能又做其他功能。
def table(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,"x",i,"=",i*j,"\t",end="")
        print()

n=int(input("请输入乘法表的层数："))
table(n)