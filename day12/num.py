def  getNum(a,b):
	try:
		c = a + b
		return c
	except Exception:
		return 4
	finally:
		return 6

num = getNum(6,9)
print(num)
