li = [1,1,1,1,3,3,3,5]

def getNum(li,index):
    if index >= len(li):
        raise AttributeError("角标超出范围！")
    else:
        return li(index)

try:
    n = getNum(li,9)
    print((n))
except IndexError:
    print("其他异常！")
except IndentationError:
    print("您访问的角标不存在！")
except ArithmeticError:
    print("算法错误!")
except Exception:
    print("这是父类异常！")


