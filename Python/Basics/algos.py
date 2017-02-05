### 
#def examine(key,value):
#	print key, ":", value

#examine(13,'food')

###

#def examine():
#	for num in range(1,100):
#		if num%3==0:
#			print "fizz"
#		elif num%5==0:
#			print "buzz"
#		if num%3==0 and num%5==0:
#			print "fizzbuzz"

#examine()

def generateCoinChange(cents):
		quarters=0
		for i in range(cents/25):
			quarters = quarters + 1
		print "quarters:", quarters 

		dimes = 0
		for i in range(cents/10):
			dimes = dimes + 1
		print "dimes:", dimes

		nickels=0
		for i in range(cents/5):
			nickels = nickels + 1
		print "nickels:", nickels

		pennies=0
		for i in range(cents/1):
			pennies = pennies + 1
		print "pennies:", pennies
			

generateCoinChange(18)