province={"010":"北京",
          "020":"上海",
          "030":"广州",
          "040":"深圳"
          }

province["010"]="安徽"
print(province)

province["050"]="常州"
print(province)
value=province["010"]
print(value)

# 获取字典中所有的键
keys=province.keys()
for key in keys:
    print(key,"=",province[key])


