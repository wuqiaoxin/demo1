# for i in range(0,8):
#     for j in range(0,i+1):
#         print("","*",end="")
#     print("")
for f in range(0,7):
    for l in range(6-f):
        print(" ",end="")
    for g in range(0,f+1):
        print("*",end=" ")
    print()

j=6
for i in range(1,8):
    print(" " * j,"* " * i)
    j = j - 1