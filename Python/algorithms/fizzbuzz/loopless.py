def count(n):
	if n >= 1:
		count(n - 1)
		fizz_buzz(n)

def fizz_buzz(n):
	if n % 15 == 0:
		print "FizzBuzz"
	elif n % 3 == 0:
		print "Fizz"
	elif n % 5 == 0:
		print "Buzz"
	else:
		print n

count(100)