class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage

	def display_all(self):
		self.tax = 0
		if self.price > 10000:
			self.tax = 15
		print "Price: " + str(self.price)
		print "Speed: " + str(self.speed)
		print "Fuel: " + str(self.fuel)
		print "Mileage: " + str(self.mileage)
		print "Tax: " + str(self.tax)


honda = Car(14000, 50, 'Full', 90)
toyota = Car(9000, 65, 'Not Full', 74)
hyundae = Car(12000, 70, 'Full', 20)
tesla = Car(20000, 80, 'Full', 15)
ford = Car(10000, 60, 'Not Full', 50)
lexus = Car(400000, 80, 'Full', 15)


honda.display_all()
toyota.display_all()
hyundae.display_all()
tesla.display_all()
ford.display_all()
lexus.display_all()

