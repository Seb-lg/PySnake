import random

from neat.neatnna import NeatNeuralNetwork
from snake import Snake, left, up, down, right
import copy
from config import SIZE
import math

def get_fit(elem):
	return elem.fitness


class Generation(object):
	def __init__(self, population, graphical=True):
		self.population = []
		self.graphical = graphical
		for i in range(population):
			nna = NeatNeuralNetwork(24, 4, 20)
			# nna.mutate()
			self.population.append(nna)
		if graphical:
			self.graph = Snake(SIZE, True)

	def run_generation(self):
		for brain in self.population:
			snake = Snake(SIZE, False)
			while not snake.update_game():
				ins = snake.get_head_lidar()
				out = brain.run(ins)
				dirm = out[0]
				dir = 0
				for i in range(4):
					if out[i] > dirm:
						dirm = out[i]
						dir = i

				newpos = None

				tmp = snake.snake[-1]
				if dir == right:
					newpos = [tmp[0] + 1, tmp[1]]
				elif dir == down:
					newpos = [tmp[0], tmp[1] + 1]
				elif dir == left:
					newpos = [tmp[0] - 1, tmp[1]]
				elif dir == up:
					newpos = [tmp[0], tmp[1] - 1]
				if not newpos in snake.snake:
					snake.direction = dir
			#brain.fitness = snake.score + snake.size * 10 + snake.food / 100# + (0 if snake.size == 3 else 500 - (snake.score/(snake.size - 3)))
			#brain.fitness = snake.score + snake.size * 10 + (0 if snake.size <= 3 else 500 - (snake.score/(snake.size - 3)))
			#brain.fitness = snake.score + snake.size * 5
			# brain.fitness = snake.size * 3 + snake.score / 2
			# brain.fitness = snake.size
			brain.fitness = snake.size #+ math.log(snake.score/100)

		self.population.sort(key=get_fit, reverse=True)

		if self.graphical:
			brain = self.population[0]
			self.graph.clear()
			while self.graph.update_graph():
				ins = self.graph.get_head_lidar()
				out = brain.run(ins)

				dirm = out[0]
				dir = 0
				for i in range(4):
					if out[i] > dirm:
						dirm = out[i]
						dir = i
				newpos = None

				tmp = self.graph.snake[-1]
				if dir == right:
					newpos = [tmp[0] + 1, tmp[1]]
				elif dir == down:
					newpos = [tmp[0], tmp[1] + 1]
				elif dir == left:
					newpos = [tmp[0] - 1, tmp[1]]
				elif dir == up:
					newpos = [tmp[0], tmp[1] - 1]
				if not newpos in self.graph.snake:
					self.graph.direction = dir

	def reproduce(self):
		for i in range(50, len(self.population)):
			mother = self.population[random.randint(0, 49)]
			self.population[i] = copy.deepcopy(mother)
			child = self.population[i]
			child.mutate()
			child.clean()
