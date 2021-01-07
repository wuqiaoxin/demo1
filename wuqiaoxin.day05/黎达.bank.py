#author:lida
import random
#银行库
bank={}
#银行的名称
bank_name="中国工商银行昌平支行"
#欢迎模板
welcome='''
*****************************
*    中国工商银行账户管理系统    *
*****************************
*1.开户                      *
*2.存钱                      *
*3.取钱                      *
*4.转账                      *
*5.查询                      *
*6.bye                      *
*****************************
'''
# print(welcome)
#随机8位取号
def getrandom():
    li=["0","1",'2','3','4','5','6','7','8','9']
    string=""
    for i in range(8):
        index=int(random.random()*len(li))    #0-10 随机获取角标
        string=string+li[index]
    return string


#银行开户逻辑
def bank_adduser(username,password,country,provinces,street,door,money,account):
    if len(bank) >=100:
        return 3
    elif account in bank:
        return 2
    else:   #account:(username:username,password:password,.....)
        bank[account]={
            "username":username,
            "password":password,
            "country":country,
            "provinces":provinces,
            "street":street,
            "door":door,
            "money":money,
            "bank_name":bank_name
        }
        return 1


#开户逻辑
def adduser():
    username=input("请输入姓名:")
    password=input("请输入密码:")
    print("接下来请输入您的地址信息：")
    country=input("请输入国家：")
    provinces=input("请输入省份：")
    street=input("请输入街道：")
    door=input("请输入门牌号：")
    money=input("请输入余额：")
    while True:
        if money.isdigit():
            money = int(money)
            break
        else:
            print("输入非法重新输入!")
            money = input("请输入余额：")
    account=getrandom()   #账号是随机的
    # print(username,password,country,provinces,street,door,money,account)
    #将上述数据传输给银行开户逻辑
    status=bank_adduser(username,password,country,provinces,street,door,money,account)
    if status==3:
        print("对不起，本银行用户库已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("对不起，您的个人信息已存在，请稍后再试")
    else:
        print("恭喜！开户成功！以下是您的开户信息：")
        info='''
        -------------开户信息--------------
        账号：{account}
        姓名：{username}
        密码：{password}
        地址信息：
            国家：{country}
            省份：{provinces}
            街道：{street}
            门牌号：{door}
        余额：{money}
        开户行名称：{bank_name}
        ----------------------------------
        '''
        #获取银行的个人信息
        user = bank[account]
        print(info.format(account=account,
                          username=user["username"],
                          password=user["password"],
                          country=user["country"],
                          provinces=user["provinces"],
                          street=user["street"],
                          door=user["door"],
                          money=user["money"],
                          bank_name=user["bank_name"]))

# #登录
# def loin():
#     account = input("请输入账号：")
#     password = input("请输入密码：")
#     if account in bank:
#         if password == bank[account]["password"]:
#
#         else:
#             return 2
#     else:
#         return 1

#银行转出逻辑
def movemoney_bank(account,password,account1,money):
    if account in bank:
        pass
        if password == bank[account]["password"]:
            pass
            if account1 in bank:
                pass
                if money <= int(bank[account]["money"]):
                    pass
                    if account == account1:
                        return 5
                    else:
                        return 0
                else:
                    return 3
            else:
                return 4
        else:
            return 2
    else:
        return 1


#用户转出逻辑
def movemoney():
    account = input("请输入转出账号：")
    password = input("请输入转出密码：")
    account1 = input("请输入转入账号：")
    money = input("请输入转出金额：")
    while True:
        if money.isdigit():
            money = int(money)
            break
        else:
            print("输入非法重新输入!")
            money = input("请输入余额：")
    status = movemoney_bank(account, password, account1, money)
    if status == 3:
        print("您的余额不足！")
    elif status == 1:
        print("您输入的转出账号不存在！")
    elif status == 4:
        print("您输入的转入账号不存在！")
    elif status == 2:
        print("您输入的密码不正确！")
    elif status == 5:
        print("转出账号和转入账号不能一致！")
    # elif status == 0:1
    else:
        money1 = int(bank[account]["money"]) - money
        bank[account]["money"]=money1
        bank[account1]["money"]=int(bank[account1]["money"]) + money
        # print("恭喜！转账成功！转账信息如下：")
        # print("您的转出金额为：", money,"您的余额为：", bank[account]["money1"])

        print("恭喜！转账成功！以下是您的转账信息：")
        info='''
        -------------转账信息--------------
        转出账号：{account}
        转入账号：{account1}
        转出金额：{money}
        账户余额：{money1}        
        ----------------------------------
        '''
        user = bank[account]
        print(info.format(account=account,
                          account1=account1,
                          money=money,
                          money1=user["money"]))

#银行查询逻辑
def find_bank(account,password,country,provinces,street,door,money):
    return 0


#用户查询逻辑
def find():
    account=input("请输入查询的账号：")
    if account in bank:
        pass
        password = input("请输入查询账号的密码：")
        if password == bank[account]["password"]:
            print("查询成功！以下是您查询得信息：")
            info = '''
            -------------开户信息--------------
            账号：{account}
            密码：{password}
            地址信息：
                国家：{country}
                省份：{provinces}
                街道：{street}
                门牌号：{door}
            余额：{money}
            开户行名称：{bank_name}
            ----------------------------------
            '''
            user = bank[account]
            print(info.format(account=account,
                              password=user["password"],
                              country=user["country"],
                              provinces=user["provinces"],
                              street=user["street"],
                              door=user["door"],
                              money=user["money"],
                              bank_name=user["bank_name"]))
        else:
            print("您输入的密码错误！")
    else:
        print("您输入的用户不存在")


#银行存钱逻辑
def savemoney_bank(account,money):
    while account in bank:
        return True
    else:
        return False




#用户存钱逻辑
def savemoney():
    account = input("请输入存钱的账号：")
    money = int(input("请输入存钱金额："))
    while True:
        if money.isdigit():
            money = int(money)
            break
        else:
            print("输入非法重新输入!")
            money = input("请输入余额：")
    status = savemoney_bank(account,money)
    if status == False:
        print("您输入的账号不存在!")
    else:
        money1 = int(int(bank[account]["money"])+money)
        bank[account]["money"] = money1
        print("存钱成功！您的余额为：",money1,"存钱金额为：",money)



#银行取钱逻辑
def getmoney_bank(account,password,money):
    if account in bank:
        if password == bank[account]["password"]:
            if money <= int(bank[account]["money"]):
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1

#用户取钱逻辑
def getmoney():
    account = input("请输入取钱账号：")
    password = input("请输入账号的密码：")
    money = int(input("请输入取钱金额："))
    while True:
        if money.isdigit():
            money = int(money)
            break
        else:
            print("输入非法重新输入!")
            money = input("请输入余额：")
    status = getmoney_bank(account,password,money)
    if status == 3:
        print("您的余额不足！无法取出！")
    elif status == 2:
        print("您输入的密码不正确！")
    elif status == 1:
        print("您输入的账号不存在！")
    else:
        money1 = int(bank[account]["money"])-money
        bank[account]["money"] = money1
        print("您取钱金额为：",money,"您的余额为：",money1)







#入口程序
while True:
    print(welcome)  #打印欢迎信息
    chose=input("请输入您的选项:")
    if chose=="1":
        adduser()     #调用开户方法完成开始adduser()
    elif chose=="2":
        savemoney()
    elif chose=="3":
        getmoney()
    elif chose=="4":
        movemoney()
    elif chose=="5":
        find()
    elif chose=="6":
        print("拜拜了您嘞！")
        break
    else:
        print("您输入的选项不存在！别瞎弄！")




















