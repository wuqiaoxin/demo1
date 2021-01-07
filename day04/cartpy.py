



shop=[
    ["iphone 8p",1000],
    ["Mac loptop",12000],
    ["IWatch",500],
    ["lenovo PC",4000],
    ["辣条",10],
    ["洗衣粉",23.5]
]
mycart=[]
# # 1、展示商城商品
# for item,value in enumerate(shop):
#     print(item,value)
# # 2、让用户输入自己的薪资
while True:
    salary=input("请输入您的薪资：")
    if salary.isdigit():
         salary=int(salary)
         break
    else:
         print("请输入合适的薪资！")
# 3、购物
while True:
    print("-------------欢迎来到商城---------------")
    for item, value in enumerate(shop):
        print(item, value)
    choose=input("请输入您选择的商品编号：")
    if choose.isdigit():
        choose=int(choose)
        if choose>len(shop):
            print("您输入的商品编号不存在！")
        else:
            if salary<shop[choose][1]:
                print("您的余额不足！")
            else:
                mycart.append(shop[choose])
                salary=salary-shop[choose][1]
                print("\033[31;20;1m您的余额为：",salary,"\033[0m")
    elif choose=="q" or choose=='Q':
        break
    else:
        print("您输入的编号不合法！")
print("-----------欢迎下次光临------------")
print("以下是您的购物信息")
for choose in mycart:
    print(choose)



