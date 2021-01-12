database={}
welcome='''
-----------------------
-1、注册
-2、登录
-3、修改密码
-4、退出系统
-----------------------
'''
def readnames():
    f=open("names.txt","r+",encoding="utf-8")
    lines=f.readlines()
    for line in lines:
        items=line.replace("\n","").split(",")
        database[items[0]]= {"username":items[0],
                             "password":items[1],
                             "sex":items[2],
                             "address":items[3],
                             "path":items[4]
        }
    f.close()

def upData(username, password, sex, age, address, path):
    readnames()
    if username in database:
        print("用户已存在！")
    else:
        database[username]={
            "username":username,
            "password":password,
            "sex":sex,
            "age":age,
            "address":address,
            "path":path
        }
def upPhoto(path):
    photo = open(path, "rb+")
    write = open("F:/ceshi-python/photo.jpg", "wb+")
    data = photo.read()
    write.write(data)
    write.close()
    photo.close()
    print("上传成功！")

def addUser():
    username = input("请输入用户名：")
    password = input("请输入密码：")
    sex = input("请输入性别：")
    age = input("请输入年龄：")
    address = input("请输入地址：")
    print("上传头像：")
    path1 = input("请输入头像路径：")
    last = ".jpg"
    path = path1 + last
    if path1 != path:
        path1 = path
    upData(username, password, sex, age, address, path)
    upPhoto(path1)

def login():
    username=input("请输入您的名字：")
    password=input("请输入您的密码：")
    if username in database:
        if password==database[username]["password"]:
            print("登录成功！")
        else:
            print("密码错误！")
    else:
        print("您输入的名字不存在！")


def changePassword():
    username = input("请输入用户名：")
    password = input("请输入原密码：")
    if username in database:
        if password == database[username]["password"]:
            password1 = input("请输入新密码：")
            database[username]["password"] = password1
            write = open("names.txt", "w+", encoding="utf-8")
            for i in database:
                for j in database[i]:
                    write.write(database[i][j])
                    if j == "path":
                        write.write("")
                    else:
                        write.write(",")
            print("修改成功！")
        else:
            print("账号或密码错误！")
    else:
        print("账号不存在！")

while True:
    print(welcome)
    choose=input("请输入您的选项：")
    if choose=="1":
        addUser()
    elif choose=="2":
        login()
    elif choose=="3":
        changePassword()
    elif choose=="4":
        print("欢迎下次再来！")
        break
    else:
        print("您输入的选项错误，重新输入")
