
name1="jason"
password1='admin'
i=2
while i>=0:
    name = input("请输入用户名：")
    password = input("请输入密码：")
    if name==name1 and password==password1:
       print("登录成功")
    else:
       print("用户名或密码错误,您还有",i,"次机会")
    i=i-1




