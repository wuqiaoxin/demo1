class User:
    __account = None
    __username = None
    __password = None
    __money = None
    __address = None
    __time = None
    __bank_name = None

    def __init__(self,account, username, password, money, time1, bank, address):
        self.__account = account
        self.__password = password
        self.__username = username
        self.__money = money
        self.__time = time1
        self.__bank_name = bank
        self.__address = address

    def setAccount(self,account):
        self.__account = account

    def getAccount(self):
        return self.__account

    def setUsername(self,username):
        self.__username = username

    def getUsername(self):
        return self.__username

    def setPassword(self,password):
         self.__password = password

    def getPassword(self):
        return self.__password

    def setMoney(self,money):
        self.__money = money

    def getMoney(self):
        return self.__money

    def setTime(self,time):
        self.__time = time

    def getTime(self):
        return self.__time

    def setBank_name(self,bank):
        self.__bank_name = bank

    def getBank_name(self):
        return self.__bank_name

    def setAddress(self,address):
        self.__address = address

    def getAddress(self):
        return self.__address

