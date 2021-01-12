# 文件读写，iso国际标准组织，utf-8




# f=open("a.txt","w+",encoding="utf-8")
# f.write("\t鹅鹅鹅")
# f.close()
# read=open("a.txt","r+",encoding="utf-8")
# write=open("F:\\b.txt","w+",encoding="utf-8")
# date=read.read()
# write.write(date)
#
# read.close()
# write.close()
read=open("a.txt","w+",encoding="utf-8")
read.write("\n\t鹅鹅鹅")
read.write("\n\t曲项向天歌。\n\t白毛浮绿水，\n\t红掌拨清波。")
read.close()


