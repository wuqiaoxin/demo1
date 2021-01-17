'''
老BB机，按键 智能手机，
打电话： 来电号码、归属地、姓名、来电铃声
新手机：打电话：来电号码、归属地、姓名、来电铃声、大头贴
'''
import time
class OldPhone:
    number = None
    def call(self,number1):
        print(self.number,"正在呼叫",number1,"来电归属地：安徽，姓名：hello,铃声：狼的诱惑")
        for i in range(6):
            print(".",end="")
            time.sleep(1)

class NewPhone(OldPhone):

    def call(self,number1):
        super().call(number1)
        print("大头贴：小猪佩奇")

phone = NewPhone()
phone.number="110"
phone.call("120")