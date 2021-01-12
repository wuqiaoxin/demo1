database= {}
f = open("b.txt","r+",encoding="utf-8")
names=f.readlines()
for item in names:
    its = item.split(",")
    database[its[0]] = its[1].replace("\n","")
# print(database)

while True:
    username=input("请输入您的用户名：")
    password=input("请输入您的密码:")
    if username in database and password==database[username]:
        print("登录成功！")
        break
    else:
        print("请输入正确的用户名和密码！")
