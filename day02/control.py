score=input("请输入你的分数：")
score=int(score)
if score>=90 and score<=100:
    print("优秀！Excellent")
elif score>=80 and score<90:
  print("良好，good")
elif score>=70 and score<80:
 print("一般般，just so so！")
elif score>=60 and score<70:
 print("及格")
elif score>=0 and score<60:
 print("不及格")
else:
 print("分数不合法")
