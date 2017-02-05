
class Bike(object):
	def __init__(self, price, speed):
		self.miles=0
		self.price=price
		self.speed=speed

	def displayinfo(self):
		print "bike price:", str(self.price)
		print "max speed:", str(self.speed)
		print "bike miles:", str(self.miles)
		return self

	def ride(self):
		print "Riding" 
		self.miles = self.miles + 10
		return self

	def reverse(self):
		print "Reversing"
		if self.miles >= 5:
			self.miles = self.miles - 5
			return self



retro = Bike(200, 25)
retro.ride().ride().ride().reverse().displayinfo()
