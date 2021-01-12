class Cup:
    __high=None
    __contain=None
    __color=None
    __quality=None

    def __init__(self,high,contain,color,quality):
        print("hello!")
        self.__high=high
        self.__contain=contain
        self.__color=color
        self.__quality=quality

    def setHigh(self,high):
        self.__high=high
    def getHigh(self):
        return self.__high

    def setContain(self,contain):
        self.__contain=contain
    def getContain(self):
        return self.__contain

    def setColor(self,color):
        self.__color=color
    def getColor(self):
        return self.__color

    def setQuality(self,quality):
        self.__quality=quality
    def getQuality(self):
        return self.__quality

    def saveLiquid(self,quan):
        print(self.__high,"cm高度的",self.__contain,"ml容积",self.__quality,"材质",self.__color,"颜色的杯子能存储",quan,"水")


cup=Cup(15,200,"粉红","glass")
print(cup.saveLiquid("可乐"))