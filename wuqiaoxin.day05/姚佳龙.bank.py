# author:yjl
import random
# 银行库
bank = {}
# 银行名称
bank_name = "中国工商银行昌平支行"
# 欢迎模板
welcome = '''
*****************************************
*         中国工商银行账户管理系统          *
*****************************************
*   1.开户                               *
*   2.存钱                               *
*   3.取钱                               *
*   4.转账                               *
*   5.查询                               *
*   6.Bye                               *
*****************************************
'''
# 随机8位账号
def getRandom():
    li = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    string = ""
    for i in range(8):
        string = string + li[int(random.random() * len(li))]
    return string

# 银行的开户逻辑
def bank_addUser(username, password, country, province, street, door, money, account):
    if len(bank) >= 100:
        return 3
    elif account in bank:
        return 2
    else:  # account : {username:username,password:password,.....}
        bank[account] = {
            "username": username,
            "password": password,
            "country": country,
            "province": province,
            "street": street,
            "door": door,
            "money": money,
            "bank_name": bank_name
        }
        return 1

# 开户逻辑
def addUser():
    username = input("请输入姓名：")
    password = input("请输入密码：")
    print("接下来输入地址：")
    country = input("请输入国家：")
    province = input("请输入省份：")
    street = input("请输入街道：")
    door = input("请输入门牌号：")
    money = input("请输入余额：")
    while True:
        if money.isdigit():
            money = int(money)
            break
        else:
            print("输入非法重新输入：")
            money = input("请输入余额：")
    account = getRandom()
    # 将上述数据传输给银行开户逻辑
    status = bank_addUser(username, password, country, province, street, door, money, account)
    if status == 3:
        print("对不起，本银行用户库已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("对不起，您的个人信息已存在！请稍后再试！")
    elif status == 1:
        info = '''
                ----------------开户信息----------------
                账号：{account}
                姓名：{username}
                密码：{password}
                地址信息：
                    国家：{country}
                    省份：{province}
                    街道：{street}
                    门牌号：{door}
                余额：{money}
                开户行名称：{bank_name}
                ----------------------------------------
            '''
        print("恭喜！开户成功！一下是您的开户信息：")

        # 获取银行的个人信息
        user = bank[account]
        print(info.format(account=account,
                          username=user["username"],
                          password=user["password"],
                          country=user["country"],
                          province=user["province"],
                          street=user["street"],
                          door=user["door"],
                          money=user["money"],
                          bank_name=user["bank_name"]))

# 登录
def login():
    account = input("请输入账号：")
    password = input("请输入密码：")
    if account in bank:
        if bank[account]["password"] == password:
            return account
        else:
            return 2
    else:
        return 1

# 银行存钱逻辑
def loseMoney_bank(money, account):
    bank[account]["money"] = bank[account]["money"] + money
    return True

# 存钱逻辑
def loseMoney():
    status = login()
    if status == 1:
        print("账号不存在！")
    elif status == 2:
        print("账号密码不匹配！")
    else:
        money = input("请输入存款金额：")
        while True:
            if money.isdigit():
                money = int(money)
                break
            else:
                print("输入非法重新输入：")
                money = input("请输入存款金额：")
        if loseMoney_bank(money, status):
            print("存款成功！您的余额为：", bank[status]["money"])

# 银行取钱逻辑
def getMoney_bank(money,account):
    if money > bank[account]["money"]:
        return 3
    else:
        return 0


# 取钱逻辑
def getMoney():
    status = login()
    if status == 1:
        print("账号不存在！")
    elif status == 2:
        print("账号密码不匹配！")
    else:
        money = input("请输入取款金额：")
        while True:
            if money.isdigit():
                money = int(money)
                break
            else:
                print("输入非法重新输入：")
                money = input("请输入取款金额：")
        status1 = getMoney_bank(money, status)
        if status1 == 3:
            print("余额不足！")
        else:
            bank[status]["money"] = bank[status]["money"] - money
            print("取款成功！余额为：", bank[status]["money"])

# 银行转账逻辑
def moveMoney_bank(account, account1, money):
    if money > bank[account]["money"]:
        return 3
    else:
        bank[account]["money"] = bank[account]["money"] - money
        bank[account1]["money"] = bank[account1]["money"] + money
        return 0


# 转账逻辑
def moveMoney():
    status = login()
    if status == 1:
        print("账号不存在！")
    elif status == 2:
        print("账号密码不匹配！")
    else:
        account1 = input("请输入收钱人账号：")
        if account1 in bank and account1 != status:
            money = input("请输入转账金额：：")
            while True:
                if money.isdigit():
                    money = int(money)
                    break
                else:
                    print("输入非法重新输入：")
                    money = input("请输入转账金额：")
            status1 = moveMoney_bank(status, account1, money)
            if status1 == 3:
                print("余额不足，无法转账！")
            else:
                print("转账成功！您的余额为：", bank[status]["money"])
        elif account1 == status:
            print("收钱人不能是自己！")
        else:
            print("收钱人账号不存在！")


# 查询逻辑
def find():
    status = login()
    if status == 1:
        print("账号不存在！")
    elif status == 2:
        print("账号密码不匹配！")
    else:
        info = '''
                        ----------------用户信息----------------
                        账号：{account}
                        姓名：{username}
                        密码：{password}
                        地址信息：
                            国家：{country}
                            省份：{province}
                            街道：{street}
                            门牌号：{door}
                        余额：{money}
                        开户行名称：{bank_name}
                        ----------------------------------------
                    '''

        # 获取银行的个人信息
        user = bank[status]
        print(info.format(account=status,
                          username=user["username"],
                          password=user["password"],
                          country=user["country"],
                          province=user["province"],
                          street=user["street"],
                          door=user["door"],
                          money=user["money"],
                          bank_name=user["bank_name"]))

# 入口程序
while True:
    print(welcome)
    chose = input("请输入您的选项：")
    if chose == "1":
        addUser()
    elif chose == "2":
        loseMoney()
    elif chose == "3":
        getMoney()
    elif chose == "4":
        moveMoney()
    elif chose == "5":
        find()
    elif chose == "6":
        print("恭喜发财！不送！")
        break
    else:
        print("您输入的选项不存在！")