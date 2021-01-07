#for i in range(0,11,2):
#   print(i)

# for i in range(0,5):
#     for j in range(0,i+1):
#         print("*",end="")
#     print()

# for i in range(0,12):
#     for j in range(1,i+1):
#         print(j,"x",i,"=",(i*j),"\t",end="")
#     print()

a=[1,2,5,6,8,10,12]
# 求所有的和a[]
# sum=0
# for i in range(0,len(a)):
#     sum=sum+a[i]
# print("和为：",sum)
# 求偶数的和
# sum1=0
# for i in range(0,len(a)):
#     if a[i] %2 !=0:
#         sum1=sum1+a[i]
# print("奇数的和为：",sum1)
# 求最大值
i=0
for k in range(0,len(a)):
    if a[k]>i:
        i=a[k]
print("最大值为：",i)

