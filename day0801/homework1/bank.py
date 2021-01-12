import random,time

from PycharmProjects.pythonProject.day0801.homework1.user import User
from PycharmProjects.pythonProject.day0801.homework1.money import Money
from PycharmProjects.pythonProject.day0801.homework1.interface import Interface
from PycharmProjects.pythonProject.day0801.homework1.address import Address

def inquire():
    file = open("users.txt", "r+", encoding="utf-8")
    a = Money()
    account = input("请输入账号：")
    password = input("请输入密码：")
    database = a.getDatabase()
    names = file.readlines()
    for item in names:
        its = item.split(",")
        database[its[0]] = {
            "account": its[0],
            "username": its[1],
            "password": its[2],
            "country": its[3],
            "province": its[4],
            "street": its[5],
            "door": its[6],
            "money": int(its[7]),
            "bank_name": its[8],
            "time": its[9]
        }
    file.close()
    a.inquire_bank(account, password)

def move():
    file = open("users.txt", "r+", encoding="utf-8")
    a = Money()
    account = input("请输入账号：")
    password = input("请输入密码：")
    account1 = input("请输入转入账号：")
    money = input("请输入转账金额：")
    while True:
        if money.isdigit():
            money = int(money)
            break
        else:
            print("输入非法重新输入：")
            money = input("请输入转账金额：")
    database = a.getDatabase()
    names = file.readlines()
    for item in names:
        its = item.split(",")
        database[its[0]] = {
            "account": its[0],
            "username": its[1],
            "password": its[2],
            "country": its[3],
            "province": its[4],
            "street": its[5],
            "door": its[6],
            "money": int(its[7]),
            "bank_name": its[8],
            "time": its[9]
        }
    file.close()
    status = a.move_bank(account, account1, password, money)
    if status == 1:
        print("输入的转入账号不存在！")
    elif status == 2:
        print("账号密码错误！")
    elif status == 3:
        print("余额不足！")
    elif status == 4:
        print("账号不存在！")
    else:
        print("转账成功！您的余额为：",database[account]["money"])


def getmoney():
    file = open("users.txt", "r+", encoding="utf-8")
    a = Money()
    account = input("请输入账号：")
    password = input("请输入密码：")
    database = a.getDatabase()
    names = file.readlines()
    for item in names:
        its = item.split(",")
        database[its[0]] = {
            "account": its[0],
            "username": its[1],
            "password": its[2],
            "country": its[3],
            "province": its[4],
            "street": its[5],
            "door": its[6],
            "money": int(its[7]),
            "bank_name": its[8],
            "time": its[9]
        }
    file.close()
    status = a.getmoney_bank(account, password)
    if status == 1:
        print("账号不存在！")
    elif status == 2:
        print("账号或密码错误！")
    elif status == 3:
        print("余额不足！")
    else:
        print("取款成功！您的余额为：", database[account]["money"])

def save():
    file = open("users.txt","r+",encoding="utf-8")
    a = Money()
    account = input("请输入账号：")
    password = input("请输入密码：")
    database = a.getDatabase()
    names = file.readlines()
    for item in names:
        its = item.split(",")
        database[its[0]] = {
            "account": its[0],
            "username": its[1],
            "password": its[2],
            "country": its[3],
            "province": its[4],
            "street": its[5],
            "door": its[6],
            "money": int(its[7]),
            "bank_name": its[8],
            "time": its[9]
        }
    file.close()

    if account in database:
        if password == database[account]["password"]:
            money = input("请输入金额：")
            while True:
                if money.isdigit():
                    money = int(money)
                    break
                else:
                    print("输入非法重新输入：")
                    money = input("请输入余额：")
            if a.save_bank(account, money):
                print("存款成功！您的余额为：", database[account]["money"])
        else:
            print("账号或密码错误！")
    else:
        print("账号不存在！")



def getRandom():
    li = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    string = ""
    for i in range(8):
        string = string + li[int(random.random() * len(li))]
    return string

def addUser():
    c = Money()
    account = getRandom()
    username = input("请输入姓名：")
    while True:
        password = input("请输入密码：")
        if len(password) != 6:
            print("输入不等于6位")
        else:
            if password.isdigit():
                break
            else:
                print("输入非法！")
    print("下面输入地址：")
    country = input("国家：")
    province = input("省份：")
    street = input("街道：")
    door = input("门牌号：")
    money = input("请输入余额：")
    while True:
        if money.isdigit():
            money = int(money)
            break
        else:
            print("输入非法重新输入：")
            money = input("请输入余额：")
    time1 = time.asctime(time.localtime(time.time()))
    bank = "中国工商银行昌平支行"
    address = Address(country, province, street, door)
    a = User(account, username, password, money, time1, bank, address)
    status = c.bank_addUser(a.getAccount(), a.getUsername(), a.getPassword(), a.getMoney(), a.getTime(), a.getBank_name(), a.getAddress().getCountry(), a.getAddress().getProvince(), a.getAddress().getStreet(), a.getAddress().getDoor())
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
                开户时间：{time}
                ----------------------------------------
            '''
        print("恭喜！开户成功！一下是您的开户信息：")
        database = c.getDatabase()
        # 获取银行的个人信息
        print(info.format(account=account,
                          username=database[account]["username"],
                          password=database[account]["password"],
                          country=database[account]["country"],
                          province=database[account]["province"],
                          street=database[account]["street"],
                          door=database[account]["door"],
                          money=database[account]["money"],
                          bank_name=database[account]["bank_name"],
                          time=database[account]["time"]))

while True:
    a = Interface()
    welcome = a.getWelcome()
    print(welcome)
    chose = input("请输入您的选项：")
    if chose == "1":
        addUser()
    elif chose == "2":
        save()
    elif chose == "3":
        getmoney()
    elif chose == "4":
        move()
    elif chose == "5":
        inquire()
    elif chose == "6":
        print("恭喜发财！不送！")
        break
    else:
        print("您输入的选项不存在！")