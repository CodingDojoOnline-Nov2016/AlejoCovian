class Fraction:
	def __init__(self,top,bottom):
		self.num = top
		self.den = bottom
	def __str__(self):
		return str(self.num)+"/"+str(self.den)