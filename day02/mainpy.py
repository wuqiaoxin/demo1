username='吴乔歆'
high=160
weight=65
age=27
sex='女'
print("我叫",username,",性别",sex,"，身高",high,"cm,体重",weight,"kg,年龄",age,"岁。")



info='''
---------------个人信息展示---------------
姓名：{username}
性别：{sex}
身高：{high}cm
体重：{weight}kg
年龄：{age}岁
-----------------------------------------
'''
print(info.format(username=username,sex=sex,high=high,weight=weight,age=age))