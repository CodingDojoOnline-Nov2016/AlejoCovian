def drawLeftChars(num,char):
	blank = ""
	spacerange = 75-num
	for i in range(num):
		blank+= char
	for i in range(spacerange):
		blank+= " "
	print blank


def drawRightChars(num,char):
	blank = ""
	spacerange = 75-num
	for i in range(spacerange):
		blank+= " "
	for i in range(num):
		blank+= char

	print blank

def drawCentreChars(num,char):
	blank = ""
	spacerange = 75-num
	for i in range(spacerange/2):
		blank+=" "
	for i in range(num):
		blank += char
	for i in range(spacerange/2):
		blank+=" "
	print blank

drawLeftChars(7, 'A')
drawRightChars(7, 'B')
drawCentreChars(7, 'C')