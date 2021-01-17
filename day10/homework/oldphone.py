class OldPhone:
    __sign=None

    def setSign(self,sign):
        self.__sign=sign

    def getSign(self):
        return self.__sign

    def call(self,number):
        print("正在给",number,"打电话！")

