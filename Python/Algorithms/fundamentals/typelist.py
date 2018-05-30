my_list = ['magical unicorns',19,'hello',98.99,'world']
strthing = " "
intthing = 0
for i in my_list:
    if type(i)==str:
        strthing += i + " "
    elif type(i)==int or type(i)==float:
        intthing += i
print ("String: ", strthing, "Number: ", intthing)
