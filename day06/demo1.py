data={}
picture=input("请输入图片的路径：")
read=open(picture,"rb+")
write=open("F:\ceshi-python\photo.jpg","wb+")
datas=read.read()
write.write(datas)
read.close()
write.close()
print("上传成功！")
# path1 = input("请输入图片的路径(图片格式jpg)：")
# last = ".JPG"
# path = path1 + last
# if path1 != path:
#     path1 = path
# photo = open(path1,"rb+")
# write = open("F:/photo.JPG", "wb+")
# data = photo.read()
# write.write(data)
# write.close()
# photo.close()
# print("上传成功！")