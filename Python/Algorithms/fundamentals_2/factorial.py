def factorial(num):
	factorial = 1
	for i in range(1, num+1):
		factorial *= i
		print factorial

factorial(4)