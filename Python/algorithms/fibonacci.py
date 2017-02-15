#FIBONACCI UTILISED WITH RECURSION:

def fibonacci(n):
	if n == 1:
		return 1
	elif n == 2:
		return 1
	elif n > 2:
		return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 11):
	print n,":", fibonacci(n)

#FIBONACCI UTILISED WITH MEMOIZATION:

fibonacci_cache = {} #dictionary stores recent function calls
def fibonacci(n):
	if n in fibonacci_cache:
		return fibonacci_cache[n]

	if n == 1:
		value = 1
	elif n == 2:
		value = 1
	elif n > 2:
		value = fibonacci(n-1) + fibonacci(n-2)

	fibonacci_cache[n] = value
	return value

for n in range(1, 11):
	print n,":", fibonacci(n)
