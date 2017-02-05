user_input = input("Enter a score: ")

for count in range(0,1):
	if(user_input<60):
		print "Grade is an F"
	elif(user_input<70):
		print "Grade is a D"
	elif(user_input<80):
		print "Grade is a C"
	elif(user_input<90):
		print "Grade is a B"
	else:
		print "Grade is an A"