def select(self,sql,param,mode="all",size="1"):
    self.cursor.execute(sql,param)
    if mode=="all":
        return self.cursor.fetchall()
    elif mode=="many":
        return self.cursor.fetchmany(size)
    elif mode=="one":
        return self.cursor.fetchone()

    def releaseConnection(self):
        self.con.commit()
        self.cursor.close()
        self.con.close()
'''
将银行的系统的数据库全部迁移到MYSQL的数据库中
a):用户类：账户(int),姓名（str),密码（6位数），地址对象，存款余额（double）、
（date）开户行，银行的名称（string）
    t_user:
    ID int auto_increment primary key;
    account int,
    username varchar(50),
    password int,
    address varchar(200),
    money double(9,2),
    registerDate date,
    bankName Varchar(70)
    
b):地址类：国家（string）、省份（string）、街道（string）、门牌号（string）
'''




# def select(self, sql, mode="1"):
#     self.cursor.execute(sql)
#     if mode == "1":
#         result = self.cursor.fetchone()
#         print(result)
#         self.cursor.close()
#         self.con.close()
#     elif mode == "2":
#         num = int(input("请输入打印几行数据:"))
#         result = self.cursor.fetchmany(num)
#         for i in result:
#             print(i)
#         self.cursor.close()
#         self.con.close()
#     else:
#         result = self.cursor.fetchall()
#         for i in result:
#             print(i)
#         self.cursor.close()
#         self.con.close()