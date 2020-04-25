class Snake:

	def __init__(self, size):
		self.x = 3 * size
		self.y = 3 * size
		self.vx = 1
		self.vy = 0
		self.size = size

		self.body = [
			(self.x - size, self.y),
			(self.x - size * 2, self.y)
		]

	def action(self, key):
		if key == "w" and self.vy != 1:
			self.vx = 0
			self.vy = -1
		if key == "a" and self.vx != 1:
			self.vx = -1
			self.vy = 0
		if key == "s" and self.vy != -1:
			self.vx = 0
			self.vy = 1
		if key == "d" and self.vx != -1:
			self.vx = 1
			self.vy = 0

	def update(self):
		self.body.pop(0)
		self.body.append((self.x, self.y))
		self.x += self.vx * self.size
		self.y += self.vy * self.size

	def grow(self):
		self.body.insert(0, self.body[0])

	def draw(self):
		fill(255)
		rect(self.x, self.y, self.size, self.size)
		for part in self.body:
			rect(part[0], part[1], self.size, self.size)