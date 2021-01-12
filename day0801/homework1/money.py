class Money:
    __database = {}
    bank_name = "中国工商银行昌平支行"

    def getDatabase(self):
        return self.__database

    def setDatabase(self,database):
        self.__database = database

    def bank_addUser(self,account, username, password, money, time1, bank, country, province, street, door):
        file = open("users.txt","a+",encoding="utf-8")
        a = Money()
        database = a.getDatabase()
        if len(database) >= 100:
            return 3
        elif account in database:
            return 2
        else:  # account : {username:username,password:password,.....}
            database[account] = {
                "account":  account,
                "username": username,
                "password": password,
                "country": country,
                "province": province,
                "street": street,
                "door": door,
                "money": money,
                "bank_name": bank,
                "time": time1
            }
            a.setDatabase(database)
            database = a.getDatabase()
            for i in database[account]:
                if i == "money":
                    file.write(str(database[account][i]))
                    file.write(",")
                else:
                    if i == "time":
                        file.write(database[account][i])
                        file.write("\r")
                    else:
                        file.write(database[account][i])
                        file.write(",")
            return 1

    def save_bank(self, account, money):
        file = open("users.txt","w+",encoding="utf-8")
        file1 = open("users.txt", "r+", encoding="utf-8")
        a = Money()
        database = a.getDatabase()
        names = file1.readlines()
        for item in names:
            its = item.split(",")
            database[its[0]] = {
                "account": its[0],
                "username": its[1],
                "password": its[2],
                "country": its[3],
                "province": its[4],
                "street": its[5],
                "door": its[6],
                "money": int(its[7]),
                "bank_name": its[8],
                "time": its[9]
            }

        database[account]["money"] = database[account]["money"] + money
        a.setDatabase(database)
        database = a.getDatabase()
        for i in database:
            for j in database[i]:
                if j == "money":
                    file.write(str(database[i][j]))
                    file.write(",")
                else:
                    if j == "time":
                        file.write(database[i][j])
                    else:
                        file.write(database[i][j])
                        file.write(",")
        file1.close()
        file.close()
        return True

    def getmoney_bank(self,account, password):
        file = open("users.txt", "w+", encoding="utf-8")
        file1 = open("users.txt", "r+", encoding="utf-8")
        a = Money()
        database = a.getDatabase()
        names = file1.readlines()
        for item in names:
            its = item.split(",")
            database[its[0]] = {
                "account": its[0],
                "username": its[1],
                "password": its[2],
                "country": its[3],
                "province": its[4],
                "street": its[5],
                "door": its[6],
                "money": int(its[7]),
                "bank_name": its[8],
                "time": its[9]
            }
        if account in database:
            if password == database[account]["password"]:
                money = input("请输入金额：")
                while True:
                    if money.isdigit():
                        money = int(money)
                        break
                    else:
                        print("输入非法重新输入：")
                        money = input("请输入金额：")
                if money > database[account]["money"]:
                    return 3
                else:
                    database[account]["money"] = database[account]["money"] - money
                    a.setDatabase(database)

                    database = a.getDatabase()
                    for i in database:
                        for j in database[i]:

                            if j == "money":
                                file.write(str(database[i][j]))
                                file.write(",")
                            else:
                                if j == "time":
                                    file.write(database[i][j])
                                else:
                                    file.write(database[i][j])
                                    file.write(",")
                    file1.close()
                    file.close()
                    return 0
            else:
                return 2
        else:
            return 1



    def move_bank(self,account, account1, password, money):
        file1 = open("users.txt", "r+", encoding="utf-8")
        a = Money()
        database = a.getDatabase()
        names = file1.readlines()
        for item in names:
            its = item.split(",")
            database[its[0]] = {
                "account": its[0],
                "username": its[1],
                "password": its[2],
                "country": its[3],
                "province": its[4],
                "street": its[5],
                "door": its[6],
                "money": int(its[7]),
                "bank_name": its[8],
                "time": its[9]
            }
        if account in database:
            if account1 in database:
                if password == database[account]["password"]:
                    if money > database[account]["money"]:
                        return 3
                    else:
                        file = open("users.txt", "w+", encoding="utf-8")
                        database[account]["money"] = database[account]["money"] - money
                        database[account1]["money"] = database[account1]["money"] + money
                        a.setDatabase(database)
                        database = a.getDatabase()
                        for i in database:
                            for j in database[i]:
                                if j == "money":
                                    file.write(str(database[i][j]))
                                    file.write(",")
                                else:
                                    if j == "time":
                                        file.write(database[i][j])
                                    else:
                                        file.write(database[i][j])
                                        file.write(",")
                        file1.close()
                        file.close()
                        return 0
                else:
                    return 2
            else:
                return 1
        else:
            return 4

    def inquire_bank(self,account, password):
        file1 = open("users.txt", "r+", encoding="utf-8")
        a = Money()
        database = a.getDatabase()
        names = file1.readlines()
        for item in names:
            its = item.split(",")
            database[its[0]] = {
                "account": its[0],
                "username": its[1],
                "password": its[2],
                "country": its[3],
                "province": its[4],
                "street": its[5],
                "door": its[6],
                "money": int(its[7]),
                "bank_name": its[8],
                "time": its[9]
            }
        file1.close()
        if account in database:
            if password == database[account]["password"]:
                info = '''
                                ----------------用户信息----------------
                                账号：{account}
                                姓名：{username}
                                密码：{password}
                                地址信息：
                                    国家：{country}
                                    省份：{province}
                                    街道：{street}
                                    门牌号：{door}
                                余额：{money}
                                开户行名称：{bank_name}
                                开户时间：{time}
                                ----------------------------------------
                            '''
                print("以下是您的开户信息：")
                database = a.getDatabase()
                # 获取银行的个人信息
                print(info.format(account=account,
                                  username=database[account]["username"],
                                  password=database[account]["password"],
                                  country=database[account]["country"],
                                  province=database[account]["province"],
                                  street=database[account]["street"],
                                  door=database[account]["door"],
                                  money=database[account]["money"],
                                  bank_name=database[account]["bank_name"],
                                  time=database[account]["time"]))
            else:
                print("账号密码错误！")
        else:
            print("账号不存在！")