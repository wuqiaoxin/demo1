import pymysql
con = pymysql.connect(host="localhost",user="root",password="",database="company")
cursor=con.cursor()
sql = "insert into t_dept values('60','sales','北京')"
result=cursor.execute(sql)
print(result)

con.commit()
cursor.close()
con.close()
