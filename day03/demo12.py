# 有下列人员数据库，请按要求实现
# # # 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["何登勇","56","男","106","IBM", 500 ,"50"],
    ["曹东雪","19","女","230","微软", 501 ,"60"],
    ["刘营营", "19", "女", "210", "Oracle", 600, "60"],
    ["李汉聪", "45", "男", "230", "Tencent", 700 , "10"]
]

# names.append(["张佳伟",45,"男","220","alibaba",500,30])
# print(names)

sum=0
for i in range(0,len(names)):
    sum=sum+names[i][5]
print("每个人的平均成绩为：",sum/len(names))

age=0
for j in range(0,len(names)):
    age=age+int(names[j][1])
print("每个人的平均年龄为：",age/len(names))

men=0
women=0
for f in range(0,len(names)):
    if names[f][2]=='男':
        men=men+1
    else:
        women=women+1
print("男生的人数为：",men,"人","\t","女生的人数为：",women,"人")

do50=0
do60=0
do10=0
do30=0
for m in range(0,len(names)):
    if names[m][6]=="50":
        do50=do50+1
    elif names[m][6]=="60":
        do60=do60+1
    elif names[m][6]=="10":
        do10=do10+1
    elif names[m][6]=="30":
        do30=do30+1
print("50这个部门的人数为：",do50,"人")
print("60这个部门的人数为：",do60,"人")
print("10这个部门的人数为：",do10,"人")
print("30这个部门的人数为：",do30,"人")


