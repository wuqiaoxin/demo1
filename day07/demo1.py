list = [21, 21, 21, 56, 56, 56, 56, 56, 56, 56, 56, 56, 10, 10, 10]
database = {}
def num(list):
    for i, j in enumerate(list):
        if j in list[0:i]:
            continue
        num = list.count(j)
        database[j] = num

num(list)
print(database)