def draw_left_stars(num):
	spacerange = 75-num
	blank = ""
	for i in range(num):
		blank += "*"
	for i in range(spacerange):
		blank += " "
	print blank

def draw_right_stars(num):
	spacerange = 75-num
	blank = ""
	for i in range(spacerange):
		blank += " "
	for i in range(num):
		blank += "*"
	print blank

def draw_centre_stars(num):
	spacerange = 75-num
	blank = ""
	for i in range(spacerange/2):
		blank += " "
	for i in range(num):
		blank += "*"
	for i in range(spacerange/2):
		blank += " "
	print blank

draw_right_stars(27)
draw_left_stars(17)
draw_centre_stars(20)