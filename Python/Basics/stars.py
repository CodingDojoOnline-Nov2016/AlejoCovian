#x = [4, 6, 3, 5, 7, 20]

#def draw_stars(x):
#	for i in range(len(x)):
#		x[i] = x[i] + 1
#		print '*' * x[i]
#	return x






x = [4, 'Tom', 1, 'Michael', 5, 7, 'Jimmy']
def draw_stars2(my_list):
	for thing in my_list:
		result = ''
		if type(thing) is int:
			for i in range(thing):
				result += '*'
		else:
			first_letter = thing[0].lower()
			for i in range(len(thing)):
				result += first_letter
		print result

draw_stars2(x)