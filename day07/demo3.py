# 有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）
class computer:
    __scream=18
    __price=6000
    __cpu="i5 酷睿六核"
    __save=8
    __time=30
    def setScream(self,scream):
        if scream<=0:
            print("输入非法")
        else:
            self.__scream=scream
    def getScream(self):
        return self.__scream

    def setPrice(self,price):
        if price<=0:
            print("输入钱不对！")
        else:
            self.__price=price
    def getPrice(self):
        return self.__price

    def setCpu(self,cpu):
        self.__cpu=cpu
    def getCpu(self):
        return self.__cpu

    def setSave(self,save):
        if save<=0:
            print("输入非法！")
        else:
            self.__save=save
    def getSave(self):
        return self.__save

    def setTime(self,time):
        if time<=0:
            print("输入非法！")
        else:
            self.__time=time
    def getTime(self):
        return self.__time

    def type(self):
        print(self.__price,"元的电脑可以打字!")
    def play(self):
        print(self.__price,"元的电脑可以打游戏！")
    def see(self):
        print(self.__scream,"寸的电脑可以看视频特别爽！")

p=computer()
p.setScream(100)
p.type()
p.see()