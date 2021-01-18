#使用键盘录入模拟从银行取钱，假设余额是3000元，如果录入的数据大于余额，通过给出提示：金额不足异常。
class MoneyException(Exception):
    def __init__(self,msg):
        self.msg = msg

class Getmoney:
    __money = None

    def setMoney(self,money):
        if money>3000:
            raise MoneyException("余额不足异常")
        else:
            self.__money=money
            print("取钱成功，金额为：",self.__money)

    def getMoney(self):
        return self.__money

get=Getmoney()
a = int(input("请输入您的金额："))
try:
    get.setMoney(a)
except MoneyException as r:
    print("bingo",r)


