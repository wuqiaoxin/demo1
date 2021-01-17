from oldphone import OldPhone
class NewPhone(OldPhone):
    def call(self,number):
        print("语言拨号中......")
        super().call(number)
        print(super().getSign(),"品牌的手机很好用！")