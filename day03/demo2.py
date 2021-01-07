a = [3,5,4,7,2,1,9,10,8,6]
# 对列表进行排序
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[j]<a[i]:
            c=a[j]
            a[j]=a[i]
            a[i]=c
print(a)