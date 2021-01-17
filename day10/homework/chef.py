class Chef:
    __name = None
    __age = None

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name

    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age

    def rice(self):
        print(self.__name,"在蒸饭")


class son(Chef):
    def cook(self):
        print(super().getName(),"在炒菜")

class grandSon(son):
    def cook(self):
        print(super().getAge(),"的年龄的",super().getName(),"在洗碗")


