# author:wrm
import random
#银行库
bank={}
#银行的名称
bank_name="中国工商银行昌平支行"
#欢迎模板
welcom='''
****************************
*   中国工商银行账户管理系统    *
****************************
*   1、开户                 *
*   2、存钱                 *
*   3、取钱                 *
*   4、转账                 *
*   5、查询                 *
*   6、拜拜                 *
****************************
'''

#随机8位取号
def getrandom():  #def随意定义一个值
    li=['1','2','3','4','5','6','7','8','9','0']
    string=""
    for i in range(8):
        index=int(random.random()*len(li))
        string=string+li[index]
    return string  #return的意思是返回数据给定义的值

#银行的开户逻辑
def bank_addUser(username,password,country,province,street,door,money,accont):
    if len(bank)>=100:
        return 3
    elif accont in bank:
        return 2
    else:
        bank[accont]={
            "username":username,
            "password":password,
            "country":country,
            "province":province,
            "street":street,
            "door":door,
            "money":money,
            "bank_name":bank_name,
        }
        return 1

# def find():
#     print("请输入您的账号：")
#     print("请输入您的密码：")

#开户逻辑
def addUser():#sddUser意思是"添加用户"
    username=input("请输入您的姓名：")
    password=input("请输入您的密码：")
    print("接下来请输入您的地址：")
    country=input("国家：")
    province=input("省份：")
    street=input("街道：")
    door=input("门牌号")
    money=input("请输入余额：")
    accont=getrandom()  #账号是随机获取的
    print(username,password,country,province,street,door,money,accont)
    #将上述数据传输到银行开户逻辑
    status=bank_addUser(username,password,country,province,street,door,money,accont)
    if status=="3":
        print("对不起，本行用户库已满，请您携带证件到其它银行办理")
    elif status=="2":
        print("对不起，你输入的个人信息已经存在，请稍候再试！")
    elif status=="1":
        print("恭喜你，开户成功！以下是您的开户信息")
        info='''
        ------------------------------
        账号:{accont}
        姓名:{username}
        密码:{password}
        地址信息：
            国家:{country}
            省份:{province}
            街道：{street}
            门牌号:{door}
        余额:{money}
        开户行:{bank_name}
        --------------------------------
        '''
        print("恭喜！开户成功！以下是您的开户信息：",info)
#获取银行的个人信息
        user= bank[accont]
        print(info.format(accont=accont,
                      username=user["username"],
                      password=user["password"],
                      country=user["country"],
                      province=user["province"],
                      street=user["street"],
                      door=user["door"],
                      money=user["money"],
                      bank_name=user["bank_name"]))
# 存钱逻辑
def savemoney():
    accont=input("请输入您的账号：")
    if accont in bank:
        sum=input("请输入您存的金额：")
        while True:
            if sum.isdigit():
                sum=int(sum)
                break
        money=bank[accont]["money"]+sum
        print("存款成功，您的余额为：",money)
    else:
        print("您输入的账号不存在")

# 取款逻辑
def getmoney():
    accont=input("请输入您的账号：")
    if accont in bank:
        sum1=input("请输入您要取款金额：")
        while True:
            if sum1.isdigit():
                sum1=int(sum1)
                break
            else:
                print("请输入金额：")
                sum1 = input("请输入您要取款金额：")
                if sum1 < bank[accont]["money"]:
                    sum1=bank[accont]["money"]-sum1
                    print("取款成功，您的账户现在余额为：", sum1)
                else:
                    print("您账户余额不足！")
    else:
        print("您输入的账号不存在！")
#转账逻辑
def movemoney():
    accont=input("请输入您的账号：")
    accont1=input("请输入您要转账的账号：")
    if accont in bank and accont1 in bank:
        sum2=input("请输入您要转的金额：")
        while True:
            if sum2.isdigit():
                sum2=int(sum2)
                if  sum2<=bank[accont]["money"]:
                    sum2=bank[accont1]["money"]+sum2
                    sum=bank[accont]["money"]-sum2
                    print("转账成功，您现在的账户余额为",sum2,"对方账户余额为：",sum)
                break
            else:
                print("请输入金额：")
                sum2 = input("请输入您要转的金额：")
    else:
        print("您输入的账号不存在！")
#查询逻辑
def find():
    accont=input("请输入您的账号：")
    if accont in bank:
        info = '''
                ------------------------------
                账号:{accont}
                姓名:{username}
                密码:{password}
                地址信息：
                    国家:{country}
                    省份:{province}
                    街道：{street}
                    门牌号:{door}
                余额:{money}
                开户行:{bank_name}
                --------------------------------
                '''
        user = bank[accont]
        print(info.format(accont=accont,
                          username=user["username"],
                          password=user["password"],
                          country=user["country"],
                          province=user["province"],
                          street=user["street"],
                          door=user["door"],
                          money=user["money"],
                          bank_name=user["bank_name"]))

    else:
        print("您输入的账号错误！")

#入口程序
while True:
    print(welcom)
    chose=input("请输入您的选项：")
    if chose=="1":      #开户
        addUser()
    elif chose=="2":
        savemoney()
    elif chose=="3":
        getmoney()
    elif chose=="4":
        movemoney()
    elif chose=="5":
        find()
    elif chose=="6":#退出
        print("拜拜了，您嘞！")
        break
    else:
        print("您输入的选项不存在")