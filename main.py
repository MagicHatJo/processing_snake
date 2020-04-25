from Snake import Snake
from Fruit import Fruit

WIDTH = 600
HEIGHT = 600
GRID_SIZE = 20

snake = Snake(GRID_SIZE)
fruit = Fruit(WIDTH, HEIGHT, GRID_SIZE)

def setup():
	global game_active
	size(WIDTH, HEIGHT)
	frameRate(6)
	game_active = True

def draw():
	global game_active
	background(0)
	if game_active:
		snake.update()
		snake.draw()
		if (snake.x == fruit.x and
			snake.y == fruit.y):
			snake.grow()
			fruit.move()
		fruit.draw()
		if game_over():
			game_active = False
	else:
		fill(255)
		textAlign(CENTER)
		textSize(72)
		text("Game Over", WIDTH / 2, HEIGHT / 4)
		textSize(60)
		text(str(len(snake.body) + 1), WIDTH / 2, HEIGHT / 2)

def keyPressed():
	snake.action(key)

def game_over():
	if (snake.x < 0 or snake.x >= WIDTH or
		snake.y < 0 or snake.y >= HEIGHT):
		return True
	for body in snake.body:
		if snake.x == body[0] and snake.y == body[1]:
			return True
	return False