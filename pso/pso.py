from nna.nna import NeuralNetwork
from random import uniform
from operator import itemgetter
from snake import *
from config import *


class Individu:
	def __init__(self, input, hiddenlayer, output):
		self.neuralNetwork = NeuralNetwork(input, hiddenlayer, output)
		self.speed = []
		self.best = []
		self.best_fitness = 0
		self.score = 0.0
		#self.fitnesse = uniform(0, 100)
		for i in range(len(self.neuralNetwork.dna)):
			self.speed.append(uniform(-0.01, 0.01))
		for i in range(self.neuralNetwork.dna.__len__()):
			self.best.append(self.neuralNetwork.dna[i].weight)


class PSO:
	def __init__(self, size):
		self.size = size
		self.population = []
		for i in range(size):
			self.population.append(Individu(2, [], 1))
		self.graph = Snake(SIZE, True)

	def update_weights(self):
		self.population.sort(key=lambda x: x.score, reverse=True)
		moy = [0.0] * len(self.population[0].speed)
		for elem in self.population:
			for i in range(len(elem.neuralNetwork.dna)):
				moy[i] += elem.best[i]

		for i in range(len(self.population[0].neuralNetwork.dna)):
			moy[i] = moy[i] / self.size

		for elem in self.population:
			if elem.score > elem.best_fitness:
				elem.best_fitness = elem.score
				for i in range(elem.best.__len__()):
					elem.best[i] = elem.neuralNetwork.dna[i].weight

			for i in range(len(elem.neuralNetwork.dna)):
				if i == 0 and elem == self.population[0]:
					print(elem.speed[i])
				elem.speed[i] += uniform(0.0, 0.3) * elem.best[i] + uniform(0.0, 0.2) * ((elem.neuralNetwork.dna[i].weight - self.population[0].best[i]) / 1000) + uniform(0.0, 0.1) * ((moy[i] - self.population[0].neuralNetwork.dna[i].weight) / 1000)
				if i == 0 and elem == self.population[0]:
					print(elem.speed[i])
				elem.neuralNetwork.dna[i].weight += elem.speed[i]
				if elem.neuralNetwork.dna[i].weight > 1.0:
					elem.neuralNetwork.dna[i].weight = 1.0
				elif elem.neuralNetwork.dna[i].weight < 0.0:
					elem.neuralNetwork.dna[i].weight = 0.0

	def run_generation(self, data):
		# with Pool(16) as p:
		# 	print(p.map(run_thread, self.population))

		for brain in self.population:
			brain.score = 0
			for elem in data:
				out = brain.neuralNetwork.run(elem[:-1])
				brain.score += 1 - abs(abs(elem[2]) - abs(out[0]))

		"""for brain in self.population:
			brain.score = 0
			for o in range(10):
				snake = Snake(SIZE, False)
				while not snake.update_game():
					ins = snake.get_head_lidar()
					#print(ins)
					#exit(0)
					out = brain.neuralNetwork.run(ins)
					dir = 0
					dirm = out[0]
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
				# brain.fitness = snake.score + snake.food / 10 + snake.size * 2
				brain.score += snake.score
			brain.score = brain.score / 10
		snake = Snake(SIZE, True)
		self.population.sort(key=lambda x: x.score, reverse=True)
		brain = self.population[0]
		while snake.update_graph():
			ins = snake.get_head_lidar()
			out = brain.neuralNetwork.run(ins)
			snake.direction = 0
			dirm = out[0]
			for i in range(4):
				if out[i] > dirm:
					dirm = out[i]
					snake.direction = i"""
