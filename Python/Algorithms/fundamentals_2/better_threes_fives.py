def betterThreesFives(start,end):
	sum = 0
	for i in range(start,end):
		if i % 3 == 0:
			sum += i
		elif i % 5 == 0:
			sum += i
	print sum

betterThreesFives(100,4000000)