save=input("请输入您的存钱金额：")
while True:
    if save.isdigit():
        save=int(save)
        break
    else:
        print("您输入的金额不合法，请重新输入！")
        save=input("请输入您的存钱金额：")


