class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 0
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def displayHealth(self):
		print self.name
		print self.health


animal = Animal('animal')
animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.health = 150
	def pet(self):
		self.health += 10
		return self

dog = Dog('dog').walk().walk() .walk().run().run().pet().displayHealth()

class Dragon(Animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name)
		self.health = 170
	def fly(self):
		self.health -=10
		return self
	def displayHealth(self):
		print "Grrr I am a dragon."
		super(Dragon, self).displayHealth()


dragon = Dragon('dragon').walk().walk().walk().run().run().fly().fly().displayHealth()