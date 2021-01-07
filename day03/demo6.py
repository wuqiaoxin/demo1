#用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
sum=0
sum1=1
for i in range(1,21):
    sum1=sum1*i
    sum=sum1+sum
print(sum)
# sum = 0
# sum1 = 1
# for i in range(1,21):
#     sum1 = sum1*i
#     sum = sum + sum1
# print(sum)