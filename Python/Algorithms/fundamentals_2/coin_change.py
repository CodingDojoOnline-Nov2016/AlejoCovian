def coinChange(num):
	dollars = 0
	halfdollars = 0
	quarters = 0
	dimes = 0
	nickels = 0
	pennies = 0
	while num >= 100:
		num -= 100
		dollars += 1
	while num >= 50:
		num -= 50
		halfdollars += 1
	while num >= 25:
		num -= 25
		quarters += 1
	while num >= 10:
		num -= 10
		dimes += 1
	while num >= 5:
		num -= 5
		dimes += 1
	while num >= 1:
		num -= 1
		pennies += 1
	print dollars, halfdollars, quarters, dimes, nickels, pennies

coinChange(123)

