def messyMath(num):
	sum = 1
	for i in range (num):
		if i % 3 == 0:
			pass
		if i % 7 == 0:
			sum += i + i
		elif num/i == 3:
			sum = -1
			break
		else:
			sum += i
		
	print sum


messyMath(4)

