class Interface:
    __welcome = '''
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

    def getWelcome(self):
        return self.__welcome
