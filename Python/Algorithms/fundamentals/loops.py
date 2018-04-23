for count in range(0,5):
    print ("looping - ", count)

count = 0
while count < 5:
    print ("looping - ", count)
    count += 1


for val in "string":
    if val == "i":
        continue
    print (val)

x = 3
y = x
while y > 0:
    print (y)
    y = y - 1
else:
    print ("Final else statement")
