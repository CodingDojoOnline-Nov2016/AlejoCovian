class FizzBuzz:
	def __init__(self,num):
		self.count(num)

	def count(self,num):
		if num>=1:
			self.count(num-1)
			self.fizz_buzz(num)

	def fizz_buzz(self,num):
		if num % 15 == 0:
			print "Fizzbuzz"
		elif num % 3 == 0:
			print "Fizz"
		elif num % 5 == 0:
			print "Buzz"
		else:
			print num

FizzBuzz(100)