class AgeException(Exception):
    def __init__(self,msg):
        self.msg=msg

class Person:
    # __name = None
    __age = None

    # def __init__(self,age):
    #     # self.__name = name
    #     self.__age = age
    #
    # def setName(self,name):
    #     self.__name = name
    #
    # def getName(self):
    #     return self.__name

    def setAge(self,age):
        if age<=0:
            raise AgeException("年龄不合法！")
        else:
            self.__age = age
            print("您的年龄为：",self.__age)

    def getAge(self):
        return self.__age


    # def compare(self,age):
    #     if age<=0:
    #         raise AgeException("年龄不合法！")
    #     else:
    #         print("您的年龄为：",age)


# u1=Person("吴小乔",23)
# u2=Person("吴小乔",24)
# c = Person.getAge(21)

# except AgeException as r:
#     print("对不起，您的",r)

# age = int(input("请输入一个数："))
person = Person()
try:
    person.setAge(-1)
except AgeException as r:
    print("输入非法！",r)


