# author:joyce
import random
# 银行库
bank={}
# 银行名称
bank_name="中国工商银行昌平支行"
# 欢迎模板
welcome='''
********************************
*    中国工商银行账户管理系统      *
********************************
*    1、开户                    *
*    2、存钱                    *
*    3、取钱                    *
*    4、转账                    *
*    5、查询                    *
*    6、Bye!                   *
********************************

'''
def getRandom():
    li=['1','2','3','4','5','6','7','8','9','0']
    string=""
    for i in range(8):
        index=int(random.random()*len(li))
        string=string+li[index]
    return string

def bank_addUser(username,password,country,province,street,door,money,account):
    if len(bank)>=100:
        return 3
    elif account in bank:
        return 2
    else:
        bank[account]={
            "username":username,
            "password":password,
            "country":country,
            "province":province,
            "street":street,
            "door":door,
            "money":money,
            "bank_name":bank_name
        }
        return 1

def addUser():
    username=input("请输入您的姓名：")
    password=input("请输入您的密码：")
    print("接下来要输入您的地址信息：")
    country=input("国家：")
    province=input("省份：")
    street=input("街道：")
    door=input("门牌号：")
    money=input("请输入您的余额：")
    while True:
        if money.isdigit():
            money=int(money)
            break
        else:
            print("请输入正确的金额！")
            money=input("请输入您的金额：")
    account=getRandom()#数字是随机的
    status=bank_addUser(username,password,country,province,street,door,money,account)
    if status==3:
        print("用户库已满！")
    elif status==2:
        print("用户已存在！")
    elif status==1:
        print("恭喜！开户成功，以下是你的开户信息！")
        info=f'''
        ----------------开户信息---------------
        账号：{account},
        姓名：{username},
        密码：{password},
        地址信息：
            国家：{country},
            省份：{province},
            街道：{street}，
            门牌号：{door}，
        金额：{money},
        开户行名称：{bank_name}
        '''
        user=bank[account]
        print(info.format(account=account,
                          username=user["username"],
                          password=user["password"],
                          country=user["country"],
                          province=user["province"],
                          street=user["street"],
                          door=user["door"],
                          money=user["money"],
                          bank_name=user["bank_name"]))

def saveMoney_bank(save,account):
    bank[account]["money"]=bank[account]["money"]+save
    return True
# 存钱逻辑
def saveMoney():
    account=input("请输入您的账号：")
    if account in bank:
        save = input("请输入您的存钱金额：")
        while True:
            if save.isdigit():
                save = int(save)
                break
            else:
                print("您输入的金额不合法，请重新输入！")
                save = input("请输入您的存钱金额：")
        if saveMoney_bank(save,account):
            print("存款成功，您的余额为：", bank[account]["money"])
    else:
        print("您的账号不存在！")

def getMoney_bank(get,account,password):
    if get <= bank[account]["money"]:
        bank[account]["money"] = bank[account]["money"] - get
        return 0
    else:
        return 3


# 取钱逻辑
def getMoney():
    account = input("请输入您的账号：")
    password= input("请输入您的密码：")
    if account in bank:
        if password==bank[account]["password"]:
            get =input("请输入您的取钱金额：")
            while True:
                if get.isdigit():
                   get=int(get)
                   break
                else:
                   print("您输入的金额不合法，请重新输入！")
                   get = input("请输入您的取钱金额：")
            if getMoney_bank(get,account,password)==0:
                print("取钱成功，您的余额为：",bank[account]["money"])
            else:
                print("您的钱不够！")
        else:
            print("您的密码错误！")
    else:
        print("您的账号不存在！")

# 转账的逻辑
def transfer():
    account=input("请输入您的账号:")
    if account in bank:
        password = input("请输入您的密码：")
        if password==bank[account]["password"]:
            account1 = input("请输入对方的账号：")
            if account1 in bank:
                transfermoney=input("请输入您需要转账的金额：")
                while True:
                    if transfermoney.isdigit():
                       transfermoney=int(transfermoney)
                       if transfermoney<=bank[account]["money"]:
                          bank[account]["money"]=bank[account]["money"]-transfermoney
                          bank[account1]["money"]=bank[account1]["money"]+transfermoney
                          print("转账成功！您的余额为：",bank[account]["money"],"对方账户余额为：",bank[account1]["money"])
                          break
                       else:
                          print("您的余额不足！")
                          transfermoney=input("请再次输入您需要转账的金额：")
                    else:
                       print("请输入正确的金额！")
                       transfermoney=input("请输入您需要转账的金额：")
            else:
                print("对方账户不存在！")
        else:
            print("您的密码错误")
    else:
       print("您的账号不存在！")

# 查询的逻辑
def enquire():
    account=input("请输入您的账号：")
    password=input("请输入您的密码：")
    if account in bank:
        if password==bank[account][password]:
            print("您的姓名为：",bank[account]["username"],
                  "您的密码为：",bank[account]["password"],
                  "国家：",bank[account]["country"],
                  "省份：",bank[account]["province"],
                  "街道：",bank[account]["street"],
                  "门牌号：",bank[account]["door"],
                  "您的余额为：",bank[account]["money"],
                  "开户行：",bank[account]["bank_name"])
        else:
            print("您的密码不正确！")
    else:
        print("您的账号不存在！")

# 入口程序
while True:
    print(welcome)
    chose = input("请输入您的选择：")
    if chose.isdigit():
        chose=int(chose)
        if chose==1:
           addUser()
        elif chose==2:
           saveMoney()
        elif chose == 3:
           getMoney()
        elif chose==4:
           transfer()
        elif chose==5:
           enquire()
        elif chose==6:
           print("拜拜！")
           break
        else:
           print("您输入值不存在！")
    else:
        print("请输入合法的值！")