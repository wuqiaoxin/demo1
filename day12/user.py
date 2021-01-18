#比较俩个人的方法
from UserException import UserNotExistsException
class User:
    __username =None
    __age = None
    def __init__(self,username,age):
        self.__userName =username
        self.__age = age

    def setUsername(self,username):
        self.__username = username
    def getUsername(self):
        return self.__username

    def setAge(self,age):
        self.__age=age
    def getAge(self):
        return self.__age

    def compare(self,user):
        if self.__username==user.getUsername() and self.__age==user.getAge():
            print("同一个人")
        else:
            raise UserNotExistsException("姓名或年龄不匹配")
try:
    u1 = User("jason",56)
    u2 = User("jason",52)
    u1.compare(u2)
except UserNotExistsException as r:
    print("异常！",r)
    
