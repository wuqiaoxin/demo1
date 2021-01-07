shop=[
    ["iphone 8p",1000],
    ["Mac loptop",12000],
    ["IWatch",500],
    ["lenovo PC",4000],
    ["辣条",10],
    ["洗衣粉",23.5]
]

mycart=[]
def showshop():
    for index,value in enumerate(shop):
        print(index,value)

while True:
    salary=input("请初始化您的薪资：")
    if salary.isdigit():
        salary=int(salary)
        break
    else:
        print("您的薪资不合法！")
score=0
scores=0
import random
discount=round((random.random()+8)/10,2)
while True:
    print("----------------欢迎来到商城----------------")
    showshop()
    choose=input("请输入您选择的商品编号：")
    if choose.isdigit():
        choose=int(choose)
        if choose >=len(shop):
            print("\033[41;20;1m您输入的商品编号不存在！\033[0m")
        else:
            if salary >= shop[choose][1]:
                mycart.append(shop[choose])
                salary=salary-shop[choose][1]*discount
                score=shop[choose][1]*discount+score
                if score > 0 and score < 5000:
                    scores = 200 + scores
                elif score >= 5000 and score < 10000:
                    scores = 400 + scores
                elif score > 10000:
                    scores = 600 + scores
                print("\033[32;20;1m您选择的商品是：",shop[choose],"您的余额为：",salary,"\033[0m","%.2f"%(discount*10),"折扣","您的积分为：",scores,"分")
            else:
                print("\033[41;20;1m您的余额不足！\033[0m")
    elif choose=="q" or choose=='Q':
        break
    else:
        print("\033[41;20;1m您输入的编号不合法！\033[0m")
print("----------欢迎下次再来-------------")
print("您选择的商品信息：")
for item in mycart:
    print(item)
print("您的消费金额为：",score,"您的余额为：",salary,"您的积分为：",scores,"分")








