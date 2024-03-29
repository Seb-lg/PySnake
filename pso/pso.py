from nna.nna import NeuralNetwork
from random import uniform


class Individu:
	def __init__(self, input, hiddenlayer, output):
		self.neuralNetwork = NeuralNetwork(input, hiddenlayer, output)
		self.speed = []
		self.best = []
		self.best_fitness = 1000000
		self.fitness = 0.0
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
		self.population.sort(key=lambda x: x.best_fitness)
		print("Best: ", self.population[0].best_fitness)
		print("Worst:", self.population[-1].best_fitness)

		for elem in self.population:
			if elem.fitness < elem.best_fitness:
				elem.best_fitness = elem.fitness
				for i in range(len(elem.best)):
					elem.best[i] = elem.neuralNetwork.dna[i].weight

			for i in range(len(elem.neuralNetwork.dna)):
				personnal_best = (elem.best[i] - elem.neuralNetwork.dna[i].weight)
				global_best = (self.population[0].best[i] - elem.neuralNetwork.dna[i].weight)

				elem.speed[i] = uniform(-0.2089, 0) * elem.speed[i] + uniform(-0.0787, 0) * personnal_best + uniform(0, 3.7637) * global_best

				elem.neuralNetwork.dna[i].weight = max(min(elem.speed[i] + elem.neuralNetwork.dna[i].weight, 1), -1)

	def run_generation(self, data):
		for brain in self.population:
			brain.fitness = 0.0
			for i in range(len(data)):
				out = brain.neuralNetwork.run(data[i][:-1])
				brain.fitness += pow((data[i][-1] - out[0]), 2)
			brain.fitness = (1 / len(data)) * brain.fitness
		self.population.sort(key=lambda x: x.best_fitness)
