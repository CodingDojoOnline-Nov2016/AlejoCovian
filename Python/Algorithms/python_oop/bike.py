class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print ("Price is: $" + str(self.price))
        print ("Max speed: " + str(self.max_speed) + "mph")
        print ("Total miles: " + str(self.miles)+ "miles")

    def drive(self):
        print ("Driving")
        self.miles += 10

    def reverse(self):
        print ("Reversing")
        if self.miles >= 5:
            self.miles -= 5

bike1 = Bike(99.99, 12)
bike1.drive()
bike1.drive()
bike1.drive()
bike1.reverse()
bike1.displayinfo()
