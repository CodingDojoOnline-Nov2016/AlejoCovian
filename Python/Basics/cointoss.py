import random

heads = 0
tails = 0

for num in range(0,5000):
	random_num = round(random.random())
	if random_num == 0:
		side = 'tail'
		tails = tails + 1
	else:
		side = 'head'
		heads = heads + 1
	print "Attempt #"+ str(num) + ", It's a " + str(side) + ", " + str(heads) + " heads so far and " + str(tails) + " tails so far."