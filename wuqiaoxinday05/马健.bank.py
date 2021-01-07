#author:Majian
import random
#银行库
bank = {}
#银行名称
bank_name = "中国工商银行昌平支行"
#欢迎模板
welcome = '''
************************************************
*            中国工商银行账户管理系统              *
************************************************
*  1.开户                                      *
*  2.存钱                                      *
*  3.取钱                                      *
*  4.转账                                      *
*  5.查询                                      *
*  6.拜拜                                      *
************************************************
'''


#生成随机8位数字账号
def getRandom():
    li = ['1','2','3','4','5','6','7','8''9','0']
    string = ""
    for i in range(8):
        index = int(random.random()*len(li))
        string = string + li[index]
    return  string

#银行的开户逻辑
def bank_addUser(username,password,country,province,street,door,money,account):
    if len(bank) >= 100:
        return 3
    elif account in bank:
        return 2
    else:# account : {username:username,password:password....}
        bank[account]= {
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


#添加用户
def addUser  ():
    username = input("请输入用户名：")
    password = input("请输入6位密码：")
    print("接下来要输入您的地址信息：")
    country = input("国家：")
    province = input("省份：")
    street = input("街道：")
    door = input( "门牌号：")
    money = input("请输入您的余额：")
    if money.isdigit():
        money = int(money)
    else:
        print("请输入正确的余额")
    account = getRandom()
    #将所有数据传输给银行的开户逻辑
    status = bank_addUser(username,password,country,province,street,door,money,account)
    if status == 3:
        print("对不起！本银行库已满，请携带证件到其他银行办理！")
    elif status ==2:
        print("对不起！您的个人信息已存在！请稍后再试！")
    elif status ==1 :
        print("恭喜！开户成功，以下是您的开户信息！")
        info = f'''
            ---------------------开户信息----------------
            账号：{account}
            姓名：{username},
            密码：{password},
            地址信息：
                国家：{country},
                省份：{province},
                街道：{street},
                门牌号：{door}
            余额：{money},
            开户行名称：{bank_name}
            -------------------------------------------
        '''
        #获取银行的个人信息
        user = bank[account]
        print(info.format(account=account,
                          username=user["username"],
                          password= user["password"],
                          country= user["country"],
                          province=user["province"],
                          street= user["street"],
                          door= user["door"],
                          money=user["money"],
                          bank_name=user["bank_name"]))

#登录
def save(account,password):
    while True:
        if account in bank :
            if password in bank[account]["password"]:
                return account
            else:
                print("请输入正确的密码！")
                break
        else:
            print("请输入正确的账号！")
            break

#存钱
def getin():
    account = input("请输入账号：")
    password = input("请输入密码：")
    save(account, password)
    while True:
        inmoney = int(input("请输入存款金额："))
        if inmoney > 0 :
            bankgetin(account,inmoney)
            print("存款成功，当前余额为：",bank[account]["money"])
            break
        elif inmoney < 0 :
            print("请输入正确金额！")
#银行存钱
def bankgetin(account,inmoney):
    bank[account]["money"] = int(bank[account]["money"]) + inmoney
    return True
#取钱
def getout():
    account = input("请输入账号：")
    password = input("请输入密码：")
    account = save(account,password)
    while True:
        outmoney = int(input("请输入取款金额："))
        state =bankgetout(account,outmoney)
        if outmoney > 0 :
            if state == 1:
                print("存款成功，当前余额为：",bank[account]["money"])
                break
            elif state == 2:
                print("余额不足！")
        else :
            print("请输入正确金额！")
#银行取钱
def bankgetout(account,outmoney):
    if bank[account]["money"] > outmoney:
        bank[account]["money"] =  int(bank[account]["money"]) - outmoney
        return 1
    elif bank[account]["money"] < outmoney:
        return 2

#转账
def movemoney():
    account = input("请输入账号：")
    password= input("请输入密码：")
    account = save(account,password)
    while True:
        moveaccount = print("请输入要转账的账号：")
        if moveaccount in bank["account"] and moveaccount != account:
            movemoney = int(input(print("请输入转账金额：")))
            state = movemaney(account,movemoney)
            if state == 1:
                print("转账成功！账户余额为：",bank[account]["money"])
            elif state == 2:
                print(("账户余额不足！请充值！"))
        else:
            print("请输入正确的账户信息！")


#银行转账
def movemaney(account,movemaney):
    if bank[account]["money"] > movemaney:
        bank[account]["money"]= int(bank[account]["money"]) - movemaney
        return 1
    elif bank[account]["money"] < movemaney:
        return 2

#查询
def find():
    account1 = input("请输入账号：")
    password1 = input("请输入密码：")
    account = save(account1,password1)
    state = bank[account]
    username = state["username"]
    password = state["password"]
    country = state["country"]
    province = state["province"]
    street = state["street"]
    door = state["door"]
    money = state["money"]
    bank_name = state["bank_name"]
    info = f'''
                ---------------------开户信息----------------
                账号：{account}
                姓名：{username},
                密码：{password},
                地址信息：
                    国家：{country},
                    省份：{province},
                    街道：{street},
                    门牌号：{door}
                余额：{money},
                开户行名称：{bank_name}
                -------------------------------------------
            '''
    print(info.format())




#入口程序
while True:
    print(welcome)     #打印欢迎信息
    chose = input("请输入您的选项：")
    if chose == "1":
        addUser()
    elif chose == "2":
        getin()
    elif chose == "3":
        getout()
    elif chose == "4":
        movemoney()
    elif chose == "5":
        find()
    elif chose == "6":
        print("欢迎下次光临！")
        break
    else:
        print("您输入的选项不存在！")











