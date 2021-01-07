a=int(input("请输入边长："))
b=int(input("请输入另一边长："))
c=int(input("请输入第三边长："))
if a+b>c and b+c>a and c+a>b:
    if a==b and a!=c:
        print("构成等腰三角形")
    elif b==c and b!=a:
        print("构成等腰三角形")
    elif c==a and c!=b:
        print("构成等腰三角形")
    elif a==b and b==c:
        print("构成等边三角形")
    else:
        print("构成普通三角形")
else:
    print("不构成三角形")