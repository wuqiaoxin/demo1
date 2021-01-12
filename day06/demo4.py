f=open("score.txt","r+",encoding="utf-8")
database={}
lines=f.readlines()
for line in lines:
    items= line.replace("\n","").split(" ")
    database[items[0]]=items[1:]

for i in database:
    sum=0
    values = database[i]
    for value in values:
        sum = sum + int(value)
    print(i,"总分数为：",sum)
f.close()