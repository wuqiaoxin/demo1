# print("-------------------------欢迎来到Jason水果商城系统----------------------------")
# print("**************************************************************************")
# print("水果名称              水果价格              水果品质              水果数量")
# print(" 苹果                  0.5                  A                   150")
# print(" 橘子                  0.2                  B                   5000")
# print(" 香蕉                  1.0                  A+                  6000")
# print(" 葡萄                  8.0                  A                   1000")
# print(" 牛油果                4.0                  A                   500")
# print(" 草莓                  2.0                  A+                  10000")
# print(" 柚子                  8.8                  B                   2000")
# print(" 橙子                  3.8                  A                   5000")
# print(" 樱桃                  0.8                  A                   10000")
# print(" 梨                   6.0                  B                   5000")
# print(" 西瓜                  20.0                 A                   2000")
# print(" 山竹                  8.0                  A                   5000")
# print(" 荔枝                  2.5                  A                   10000")
# print(" 龙眼                  1.0                  A                   20000")
# print(" 榴莲                  100.0                A                    500")
# print(" 哈密瓜                18.0                 A                    600")
# print(" 柠檬                  5.0                  B                    1000")
# print(" 菠萝蜜                200.0                A                    500")
# print(" 椰子                  12.0                 B                    600")
# print(" 猕猴桃                 8.0                 A                    1000")
# print(" 蓝莓                   0.3                 A                    20000")
# print(" 无花果                 4.5                 A                    2000")
# print("-----------------------------------------------------------------------")
# print(" 总金额为：",(0.5*150+0.2*5000+1*6000+8*1000+4*500+2*10000+8.8*2000+3.8*5000+0.8*10000+6*5000+20*2000+8*5000+2.5*10000+1*20000+100*500+18*600+5*1000+200*500+12*600+8*1000+0.3*20000+4.5*2000),"￥")

fruit1="苹果"
fruit2="橘子"
fruit3="香蕉"
fruit4="葡萄"
fruit5="牛油果"
fruit6="草莓"
fruit7="橙子"
fruit8="柚子"
fruit9="樱桃"
fruit10="梨"
fruit11="山竹"
fruit12="西瓜"
fruit13="荔枝"
fruit14="龙眼"
fruit15="榴莲"
fruit16="哈密瓜"
fruit17="柠檬"
fruit18="菠萝蜜"
fruit19="猕猴桃"
fruit20="蓝莓"
price1=0.5
price2=0.2
price3=8.0
price4=4.0
price5=2.0
price6=8.8
price7=3.8
price8=0.8
price9=6.0
price10=20.0
price11=8.0
price12=2.5
price13=1.0
price14=100.0
price15=18.0
price16=5.0
price17=12.0
price18=8.0
price19=0.3
price20=4.5
quality1="A"
quality2="B"
quality3="A"
quality4="A"
quality5="A+"
quality6="B"
quality7="A"
quality8="A"
quality9="B"
quality10="A"
quality11="A"
quality12="A"
quality13="A"
quality14="A"
quality15="A"
quality16="B"
quality17="B"
quality18="A"
quality19="A"
quality20="A"
quantity1=150
quantity2=5000
quantity3=1000
quantity4=500
quantity5=10000
quantity6=2000
quantity7=5000
quantity8=10000
quantity9=5000
quantity10=2000
quantity11=5000
quantity12=10000
quantity13=20000
quantity14=500
quantity15=600
quantity16=1000
quantity17=600
quantity18=1000
quantity19=20000
quantity20=2000
sum1=((quantity1*price1)+(quantity2*price2)+(quantity3*price3)+(quantity4*price4)+(quantity5*price5)+(quantity6*price6)+(quantity7*price7)+(quantity8*price8)+(quantity9*price9)+(quantity10*price10)+(quantity11*price11)+(quantity12*price12)+(quantity13*price13)+(quantity14*price14)+(quantity15*price15)+(quantity16*price16)+(quantity17*price17)+(quantity18*price18)+(quantity19*price19)+(quantity20*price20))

info='''
{fruit1}\t\t{quality1}\t\t{price1}\t\t{quantity1}
'''
print("----------------------欢迎来到Jason水果商城系统--------------------------")
print("***************************************************************************")
print("水果名称\t水果品质\t水果价格\t水果数量")
print(info.format(fruit1=fruit1,quantity1=quantity1,quality1=quality1,price1=price1))
print(info.format(fruit1=fruit2,quantity1=quantity2,quality1=quality2,price1=price2))
print(info.format(fruit1=fruit3,quantity1=quantity3,quality1=quality3,price1=price3))
print(info.format(fruit1=fruit4,quantity1=quantity4,quality1=quality4,price1=price4))
print(info.format(fruit1=fruit5,quantity1=quantity5,quality1=quality5,price1=price5))
print(info.format(fruit1=fruit6,quantity1=quantity6,quality1=quality6,price1=price6))
print(info.format(fruit1=fruit7,quantity1=quantity7,quality1=quality7,price1=price7))
print(info.format(fruit1=fruit8,quantity1=quantity8,quality1=quality8,price1=price8))
print(info.format(fruit1=fruit9,quantity1=quantity9,quality1=quality9,price1=price9))
print(info.format(fruit1=fruit10,quantity1=quantity10,quality1=quality10,price1=price10))
print(info.format(fruit1=fruit11,quantity1=quantity11,quality1=quality11,price1=price11))
print(info.format(fruit1=fruit12,quantity1=quantity12,quality1=quality12,price1=price12))
print(info.format(fruit1=fruit13,quantity1=quantity13,quality1=quality13,price1=price13))
print(info.format(fruit1=fruit14,quantity1=quantity14,quality1=quality14,price1=price14))
print(info.format(fruit1=fruit15,quantity1=quantity15,quality1=quality15,price1=price15))
print(info.format(fruit1=fruit16,quantity1=quantity16,quality1=quality16,price1=price16))
print(info.format(fruit1=fruit17,quantity1=quantity17,quality1=quality17,price1=price17))
print(info.format(fruit1=fruit18,quantity1=quantity18,quality1=quality18,price1=price18))
print(info.format(fruit1=fruit19,quantity1=quantity19,quality1=quality19,price1=price19))
print(info.format(fruit1=fruit20,quantity1=quantity20,quality1=quality20,price1=price20))
print("------------------------------------------------------------")
print("总金额为：",sum1,"￥")

