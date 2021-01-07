a=[15,20,12,63,3,8,94,61,27,5,10]#求其中是5的倍数的和
sum=0
for i in range(0,len(a)):
    if a[i]%5==0:
        sum=sum+a[i]
print(sum)

j=6
for i in range(1,8):
    print(""*j,"*"*i)
    j=j-1
