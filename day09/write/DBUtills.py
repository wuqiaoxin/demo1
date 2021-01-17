import pymysql
class DBUtills():
    user="root"
    host="localhost"
    password=""
    database="company"
    con=None
    cursor=None

    def __init__(self,user="root",host="localhost",password="",database="company"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.con = pymysql.connect(host = self.host,
                                   user = self.user,
                                   password =self.password,
                                   database =self.database)
        self.cursor = self.con.cursor()

    def updata(self, sql, param, mode="1"):
            if mode == "1":
                self.cursor.execute(sql, param)
            else:
                self.cursor.executemany(sql, param)


    def select(self,sql,param,mode="all",size=1):
        self.cursor.execute(sql, param)
        if mode == "all":
            return self.cursor.fetchall()
        elif mode == "many":
            return self.cursor.fetchmany(size)
        elif mode == "one":
            return self.cursor.fetchone()

    def releaseConnection(self):
        self.con.commit()
        self.cursor.close()
        self.con.close()




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
    #

db = DBUtills()
sql = "select * from t_employees where ename = %s"
param = ["关二爷"]
result = db.select(sql,param,mode="all")
print(result)
db.releaseConnection()
# sql = "select * from t_employees"
# mode = "2"
# a.select(sql, mode)