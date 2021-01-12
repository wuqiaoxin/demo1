f = open("baidu_x_system.log","r+", encoding="utf-8")
lines=f.readlines()
ips=[]
for line in lines:
    items=line.split(" ")
    ips.append(items[0])

for index,ip in enumerate(ips):
    if ip in ips[0:index]:
        continue
    else:
        num=ips.count(ip)
        print(ip,"出现了",num,"次")














