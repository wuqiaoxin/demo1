#书写一个计算器，有加减乘除四大方法。写一个测试类对计算器的加减乘除进行调用。
from defcalculator import Calculator
calculator=Calculator()
data ='''
----------------------
1、加法
2、减法
3、乘法
4、除法
5、退出
'''

while True:
    num1 = float(input("请输入第一个数："))
    num2 = float(input("请输入第二个数："))
    print(data)
    choose = input("请输入您的选项：")
    if choose =='1':
        print("结果为：",calculator.jia(num1,num2))
    elif choose == '2':
        print("结果为：",calculator.jian(num1,num2))
    elif choose == '3':
        print("结果为：",calculator.cheng(num1,num2))
    elif choose == '4':
        print("结果为：",calculator.chu(num1,num2))
    elif choose == '5':
        break
    else:
        print("您输入的选项不正确！请重新输入！")



