class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print("Price: ", price, "Maximum speed: ", max_speed, "Total miles: ", miles)

    def ride(self):
        miles += 10
        print("Riding")

    def reverse():
        if self.miles >= 5:
            miles -= 5
        print("Reversing")


bike1 = Bike(99.99, 12)
bike1.drive()
bike1.drive()
bike1.drive()
bike1.reverse()
bike1.displayInfo()
