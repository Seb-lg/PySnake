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
		self.best_fitness = 1000000
		self.score = 0.0
		for i in range(len(self.neuralNetwork.dna)):
			self.speed.append(uniform(-1.0, 1.0))
			self.best.append(self.neuralNetwork.dna[i].weight)


class PSO:
	def __init__(self, size, input, hidden, output):
		self.size = size
		self.population = []
		for i in range(size):
			self.population.append(Individu(input, hidden, output))

	def update_weights(self):
		self.population.sort(key=lambda x: x.best_fitness)#, reverse=True)
		print("HERE: ", self.population[0].best_fitness)
		print("HERE: ", self.population[-1].best_fitness)
		moy = [0.0] * len(self.population[0].speed)
		for elem in self.population:
			for i in range(len(elem.neuralNetwork.dna)):
				moy[i] += elem.best[i]

		for i in range(len(self.population[0].neuralNetwork.dna)):
			moy[i] = moy[i] / self.size

		for elem in self.population:
			if elem.score < elem.best_fitness:
				elem.best_fitness = elem.score
				for i in range(elem.best.__len__()):
					elem.best[i] = elem.neuralNetwork.dna[i].weight

			for i in range(len(elem.neuralNetwork.dna)):
				a = elem.best[i]
				b = (self.population[0].best[i] - elem.neuralNetwork.dna[i].weight)
				c = (moy[i] - self.population[0].neuralNetwork.dna[i].weight)
				#elem.speed[i] = 0.5 * elem.speed[i] + uniform(0.0, 0.3) * a + uniform(0.0, 0.2) * b + uniform(0.0, 0.1) * c

				elem.neuralNetwork.dna[i].weight += elem.speed[i] + uniform(0.0, 2.0) * a + uniform(0.0, 2.0) * b + uniform(0.0, 0.1) * c
				if elem.neuralNetwork.dna[i].weight > 10.0:
					elem.neuralNetwork.dna[i].weight = 10.0
				elif elem.neuralNetwork.dna[i].weight < -10.0:
					elem.neuralNetwork.dna[i].weight = -10.0
		#print("SEMPAI " + str(self.population[0].neuralNetwork.dna[0].weight))

	def run_generation(self, data):
		# with Pool(16) as p:
		# 	print(p.map(run_thread, self.population))

		for brain in self.population:
			brain.score = 0
			for elem in data:
				out = brain.neuralNetwork.run(elem[:-1])
				brain.score += abs(elem[-1] - out[0])
				#elem.fitness += math.fabs(dta[2] - sigmoid(x))

			#brain.score += abs((elem[1] + 1) - (out[0] + 1))
			#brain.score = brain.score / len(data)
