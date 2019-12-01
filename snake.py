import pygame
import random
import time
from config import SCREEENSIZE

right = 0
down = 1
left = 2
up = 3


class Snake(object):

	def __init__(self, width, drawable):
		self.width = width
		self.time = time.time()
		if drawable:
			pygame.init()
			clock = pygame.time.Clock()
			clock.tick(20)
			self.screen = pygame.display.set_mode((SCREEENSIZE, SCREEENSIZE))
		self.board = []
		for i in range(width):
			self.board.append([0]*width)
		x = random.randint(3, self.width - 4)
		y = random.randint(3, self.width - 4)
		self.snake = [[x, y]]
		dir = random.randint(0, 3)
		if dir == left:
			self.snake.append([x - 1, y])
			self.snake.append([x - 2, y])
			self.direction = left
		elif dir == right:
			self.snake.append([x + 1, y])
			self.snake.append([x + 2, y])
			self.direction = right
		elif dir == up:
			self.snake.append([x, y - 1])
			self.snake.append([x, y - 2])
			self.direction = up
		elif dir == down:
			self.snake.append([x, y + 1])
			self.snake.append([x, y + 2])
			self.direction = down
		# 0 right
		# 1 down
		# 2 left
		# 3 up

		self.score = 0
		self.size = 3
		self.food = self.width * 3

		for pos in self.snake:
			self.board[pos[0]][pos[1]] = 2
		x = random.randint(0, self.width - 1)
		y = random.randint(0, self.width - 1)
		while self.board[x][y] != 0:
			x = random.randint(0, self.width - 1)
			y = random.randint(0, self.width - 1)
		self.board[x][y] = 1

	def clear(self):
		self.board = []
		for i in range(self.width):
			self.board.append([0] * self.width)

		x = random.randint(3, self.width - 4)
		y = random.randint(3, self.width - 4)
		self.snake = [[x, y]]
		dir = random.randint(0, 3)
		if dir == left:
			self.snake.append([x - 1, y])
			self.snake.append([x - 2, y])
			self.direction = left
		elif dir == right:
			self.snake.append([x + 1, y])
			self.snake.append([x + 2, y])
			self.direction = right
		elif dir == up:
			self.snake.append([x, y - 1])
			self.snake.append([x, y - 2])
			self.direction = up
		elif dir == down:
			self.snake.append([x, y + 1])
			self.snake.append([x, y + 2])
			self.direction = down

		for pos in self.snake:
			self.board[pos[0]][pos[1]] = 2
		x = random.randint(0, self.width - 1)
		y = random.randint(0, self.width - 1)
		while self.board[x][y] != 0:
			x = random.randint(0, self.width - 1)
			y = random.randint(0, self.width - 1)
		self.board[x][y] = 1
		self.score = 0
		self.size = 3
		self.food = self.width * 2

	def update_game(self):
		self.score += 1
		self.food -= 1
		if self.food <= 0:
			return True

		newpos = None

		tmp = self.snake[-1]
		if self.direction == right:
			newpos = [tmp[0] + 1, tmp[1]]
		elif self.direction == down:
			newpos = [tmp[0], tmp[1] + 1]
		elif self.direction == left:
			newpos = [tmp[0] - 1, tmp[1]]
		elif self.direction == up:
			newpos = [tmp[0], tmp[1] - 1]

		if newpos in self.snake or newpos[0] < 0 or newpos[1] < 0 or newpos[0] >= self.width or newpos[1] >= self.width:
			return True

		self.snake.append(newpos)
		tmp = self.snake[-1]

		if self.board[tmp[0]][tmp[1]] == 1:
			tmpx = random.randint(0, self.width - 1)
			tmpy = random.randint(0, self.width - 1)
			while self.board[tmpx][tmpy] != 0:
				tmpx = random.randint(0, self.width - 1)
				tmpy = random.randint(0, self.width - 1)
			self.board[tmpx][tmpy] = 1
			self.food += self.width * 10
			self.size += 1
		else:
			oldpos = self.snake[0]
			self.board[oldpos[0]][oldpos[1]] = 0
			self.snake = self.snake[1:]

		self.board[tmp[0]][tmp[1]] = 2

	def update_graph(self):
		self.time = time.time()
		time.sleep((1/60) - (time.time() - self.time))
		self.time = time.time()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					self.direction = right
				elif event.key == pygame.K_DOWN:
					self.direction = down
				elif event.key == pygame.K_LEFT:
					self.direction = left
				elif event.key == pygame.K_UP:
					self.direction = up

		if self.update_game():
			return

		for x in range(0, self.width):
			for y in range(0, self.width):
				width = SCREEENSIZE//self.width // 2
				dx = SCREEENSIZE//self.width * x + width
				dy = SCREEENSIZE//self.width * y + width
				if self.board[x][y] == 0:
					pygame.draw.circle(
						self.screen,
						#pygame.Color(random.randint(0, 255), random.randint(0, 255), 120),
						pygame.Color(23, 23, 23),
						(dx, dy),
						width
					)
				elif self.board[x][y] == 1:
					# POMME
					pygame.draw.circle(
						self.screen,
						pygame.Color(255, 0, 0),
						(dx, dy),
						width
					)
				elif self.board[x][y] == 2:
					#SNAKE
					pygame.draw.circle(
						self.screen,
						pygame.Color(0, 255, 0),
						(dx, dy),
						width
					)

		pygame.display.flip()
		return True

	def get_head_lidar(self):
		lidar = []
		head = self.snake[-1]

		##------------ RIGHT
		i = 1
		while head[0] + i < self.width and self.board[head[0] + i][head[1]] != 1:
			i += 1
		if head[0] + i == self.width:
			i = self.width
		lidar.append(1 - (i / self.width))
		i = 1
		while head[0] + i < self.width and self.board[head[0] + i][head[1]] != 2:
			i += 1
		if head[0] + i == self.width:
			i = self.width
		lidar.append(1 - (i / self.width))
		i = 1
		while head[0] + i < self.width:
			i += 1
		lidar.append(1 - (i / self.width))

		##------------ DOWN
		i = 1
		while head[1] + i < self.width and self.board[head[0]][head[1] + i] != 1:
			i += 1
		if head[1] + i == self.width:
			i = self.width
		lidar.append(1 - (i / self.width))
		i = 1
		while head[1] + i < self.width and self.board[head[0]][head[1] + i] != 2:
			i += 1
		if head[1] + i == self.width:
			i = self.width
		lidar.append(1 - (i / self.width))
		i = 1
		while head[1] + i < self.width:
			i += 1
		lidar.append(1 - (i / self.width))

		##------------ LEFT
		i = 1
		while head[0] - i >= 0 and self.board[head[0] - i][head[1]] != 1:
			i += 1
		if head[0] - i < 0:
			i = self.width
		lidar.append(1 - (i / self.width))
		i = 1
		while head[0] - i >= 0 and self.board[head[0] - i][head[1]] != 2:
			i += 1
		if head[0] - i < 0:
			i = self.width
		lidar.append(1 - (i / self.width))
		i = 1
		while head[0] - i >= 0:
			i += 1
		lidar.append(1 - (i / self.width))

		##------------ UP
		i = 1
		while head[1] - i >= 0 and self.board[head[0]][head[1] - i] != 1:
			i += 1
		if head[1] - i < 0:
			i = self.width
		lidar.append(1 - (i / self.width))
		i = 1
		while head[1] - i >= 0 and self.board[head[0]][head[1] - i] != 2:
			i += 1
		if head[1] - i < 0:
			i = self.width
		lidar.append(1 - (i / self.width))
		i = 1
		while head[1] - i >= 0:
			i += 1
		lidar.append(1 - (i / self.width))

		#return lidar


		# right up
		i = 1
		while head[0] + i < self.width and head[1] - i >= 0 and self.board[head[0] + i][head[1] - i] != 1:
			i += 1
		if head[0] + i == self.width:
			i = self.width
		lidar.append(1 - (i / self.width))
		i = 1
		while head[0] + i < self.width and head[1] - i >= 0 and self.board[head[0] + i][head[1] - i] != 2:
			i += 1
		if head[0] + i == self.width:
			i = self.width
		lidar.append(1 - (i / self.width))
		i = 1
		while head[0] + i < self.width and head[1] - i >= 0:
			i += 1
		lidar.append(1 - (i / self.width))

		# right down
		i = 1
		while head[0] + i < self.width and head[1] + i < self.width and self.board[head[0] + i][head[1] + i] != 1:
			i += 1
		if head[0] + i == self.width:
			i = self.width
		lidar.append(1 - (i / self.width))
		i = 1
		while head[0] + i < self.width and head[1] + i < self.width and self.board[head[0] + i][head[1] + i] != 2:
			i += 1
		if head[0] + i == self.width:
			i = self.width
		lidar.append(1 - (i / self.width))
		i = 1
		while head[0] + i < self.width and head[1] + i < self.width:
			i += 1
		lidar.append(1 - (i / self.width))

		# left down
		i = 1
		while head[0] - i >= 0 and head[1] + i < self.width and self.board[head[0] - i][head[1] + i] != 1:
			i += 1
		if head[0] - i < 0:
			i = self.width
		lidar.append(1 - (i / self.width))
		i = 1
		while head[0] - i >= 0 and head[1] + i < self.width and self.board[head[0] - i][head[1] + i] != 2:
			i += 1
		if head[0] - i < 0:
			i = self.width
		lidar.append(1 - (i / self.width))
		i = 1
		while head[0] - i >= 0 and head[1] + i < self.width:
			i += 1
		lidar.append(1 - (i / self.width))

		# left up
		i = 1
		while head[0] - i >= 0 and head[1] - i >= 0 and self.board[head[0] - i][head[1] - i] != 1:
			i += 1
		if head[0] - i < 0:
			i = self.width
		lidar.append(1 - (i / self.width))
		i = 1
		while head[0] - i >= 0 and head[1] - i >= 0 and self.board[head[0] - i][head[1] - i] != 2:
			i += 1
		if head[0] - i < 0:
			i = self.width
		lidar.append(1 - (i / self.width))
		i = 1
		while head[0] - i >= 0 and head[1] - i >= 0:
			i += 1
		lidar.append(1 - (i / self.width))

		return lidar
