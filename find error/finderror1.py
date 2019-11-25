from builtins import NotImplemented, type, super
from math import pi

class Shape:
	def area(self):
		raise NotImplemented

	def circumference(self):
		raise NotImplemented

	def __str__(self):
		print(type(self).__name__)

class Circle(Shape):

	def __init__(self, r):
		self.r = r

	def area(self):
		print(pi * self.r ** 2)

	def circumference(self):
		print(2 * pi * self.r)

class Rectangle(Shape):
	def __init__(self, length, width):
		self.l = length
		self.w = width

def area(self):
	print(self.l * self.w)
	def circumference(self):
		print(2 * self.l + 2 * self.w)

class Square(Rectangle):
	def __init__(self, length):
		super(Square, self).__init__(length, length)

shapes = [Square(10), Circle(20), Rectangle(3.4, 1.5)]
for shape in shapes:
	print('{} area is {}'.format(shape, shape.area()))
	# shape.area() эта функция вызывает ошибку (raise NotImplemented)

