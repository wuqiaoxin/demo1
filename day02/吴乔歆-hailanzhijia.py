#print("-------------------欢迎来到海澜之家品牌服装店---------------------")
#print("=============================================================")
#print("服装名称          码数              价格                数量   ")
'''
# print("格纹衬衫          S                360                500")
# print("型男T恤           M                380                600")
# print("牛仔裤            L                 500                800")
# print("弹力休闲裤        XL                520                600")
# print("翻领夹克          XXL               880                800")
# print("针织衫            XXXL             800                600")
# print("卫衣              L               860               500")
# print("羽绒服            M               2000               500")
# print("西装              L               2800               600")
# print("-----------------------------------------------------------")
# print("总金额为：",(360*500+380*600+500*800+520*600+880*800+800*600+860*500+2000*500+2800*600),"￥")
'''

num1="格纹衬衫"
size1="S"
price1=360
quantity1=500

num2="牛仔裤"
size2="L"
price2=500
quantity2=800

num3="型男T恤"
size3="M"
price3=380
quantity3=600

num4="弹力休闲裤"
size4="XL"
price4=520
quantity4=600

num5="翻领夹克"
size5="XL"
price5=880
quantity5=800

num6="针织衫 "
size6="XXL"
price6=800
quantity6=600

num7="卫衣 "
size7="XXXL"
price7=860
quantity7=500

num8="羽绒服 "
size8="XL"
price8=2000
quantity8=500

num9="西装 "
size9="XL"
price9=2800
quantity9=600




info='''
----------------------欢迎来到海澜之家品牌服装店---------------------------
======================================================================
服装名称\t\t码数\t\t价格\t\t数量
{num1}\t\t{size1}\t\t{price1}\t\t{quantity1}
{num2}\t\t{size2}\t\t{price2}\t\t{quantity2}
{num3}\t\t{size3}\t\t{price3}\t\t{quantity3}
{num4}\t{size4}\t\t{price4}\t\t{quantity4}
n{num5}\t\t{size5}\t\t{price5}\t\t{quantity5}
{num6}\t\t{size6}\t\t{price6}\t\t{quantity6}
{num7}\t\t{size7}\t{price7}\t\t{quantity7}
{num8}\t\t{size8}\t\t{price8}\t{quantity8}
{num9}\t\t{size9}\t\t{price9}\t{quantity9}
--------------------------------------------------------------------
总金额为： {sum}￥

'''
print(info.format(num1=num1,size1=size1,price1=price1,quantity1=quantity1,
                  num2=num2,size2=size2,price2=price2,quantity2=quantity2,
                  num3=num3,size3=size3,price3=price3,quantity3=quantity3,
                  num4=num4,size4=size4,price4=price4,quantity4=quantity4,
                  num5=num5,size5=size5,price5=price5,quantity5=quantity5,
                  num6=num6,size6=size6,price6=price6,quantity6=quantity6,
                  num7=num7,size7=size7,price7=price7,quantity7=quantity7,
                  num8=num8,size8=size8,price8=price8,quantity8=quantity8,
                  num9=num9,size9=size9,price9=price9,quantity9=quantity9,
                  sum=price1*quantity1+price2*quantity2+price3*quantity3+price4*quantity4+
                      price5*quantity5+price6*quantity6+price7*quantity7+price8*quantity8+price9*quantity9))


