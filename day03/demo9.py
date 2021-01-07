a=[5,2,4,7,9,1,3,5,4,0,6,1,3]#请对下列列表进行冒泡排序

# for i in range(0,len(a)):
#     for j in range(0,i+1):
#         if a[j]<a[i]:
#             c=a[j]
#             a[j]=a[i]
#             a[i]=c
# print(a)

for i in range(0,len(a)):
    for j in range(0,i+1):
        if a[j]>a[i]:
            c=a[j]
            a[j]=a[i]
            a[i]=c
print(a)
