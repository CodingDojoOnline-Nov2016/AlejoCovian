import random
def generate():
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	for i in range(100):
		res = " "
		res += alphabet[random.randrange(26)]
		if alphabet[random.randrange(26)]== 'g':
			print 'yuckyuckyuck'


generate()

