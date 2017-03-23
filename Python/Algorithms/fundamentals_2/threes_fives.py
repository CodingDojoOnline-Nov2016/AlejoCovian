sum = 0
for i in range(100, 4000000):
	if i % 3 == 0:
		sum += i 
	elif i % 5 == 0:
		sum += i
print sum