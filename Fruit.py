import random

class Fruit:

	def __init__(self, width, height, size):
		self.x = random.randint(0, width - size) // size * size
		self.y = random.randint(0, height - size) // size * size
		self.width = width
		self.height = height
		self.size = size

	def move(self):
		self.x = random.randint(0, self.width - self.size) // self.size * self.size
		self.y = random.randint(0, self.height - self.size) // self.size * self.size

	def draw(self):
		fill(200, 0, 0)
		rect(self.x, self.y, self.size, self.size)