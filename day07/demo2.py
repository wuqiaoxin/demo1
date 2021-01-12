# 高，容积，颜色，材质
# 能存放液体
class cup:
    __high=8
    __V=400
    __color="粉色"
    __quality="玻璃"


    def setHigh(self,high):
        if high<=0:
            print("输入非法")
        else:
            self.__high=high
    def getHigh(self):
        return self.__high

    def setV(self,V):
        if V<=0:
            print("输入非法！")
        else:
            self.__V=V
    def getV(self):
        return self.__V

    def setColor(self,color):
        self.__color=color
    def getColor(self):
        return self.__color

    def setQuality(self,quality):
        self.__quality=quality
    def getQuality(self):
        return self.__quality

    def water(self):
        print("高为：",self.__high,"cm",self.__color,"的杯子能存放液体！")

c=cup()
c.water()


