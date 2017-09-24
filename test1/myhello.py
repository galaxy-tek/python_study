class Worker:
	def __init__(self,name,pay):
		self.name=name
		self.pay=pay
	def lastName(self):
		return self.name.split()[-1]
	def giveRaise(self,percent):
		self.pay= self.pay*(1+percent)


def area(width, height):
	return (width * height)

bob=Worker('Bob Smith',5000)
sue=Worker('Sue Jones',6000)

print(bob.name)
print(bob.lastName())
print(bob.pay)

print('bob.giveRaise(0.1)')
bob.giveRaise(0.1)
print('bob new pay:',bob.pay)

print(sue.name)
print(sue.lastName())
print(sue.pay)
print('sue.giveRaise(0.2)')
sue.giveRaise(0.2)
print('sue new pay:',sue.pay)


