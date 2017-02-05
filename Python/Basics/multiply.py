a = [2,4,10,16]
def multiply(a,b):
	for i in range(len(a)):
		a[i] = a[i] * 5
	return a

b = multiply(a,5)
print b