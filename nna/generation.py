import random

from nna.nna import NeuralNetwork
from snake import Snake, left, up, right, down
from config import SIZE


def get_fit(elem):
	return elem.fitness

prcent = 10


class Generation(object):
	def __init__(self, population):

		self.population = []
		for i in range(population):
			self.population.append(NeuralNetwork(24, [20, 12], 4))

	def run_generation(self):
		# with Pool(16) as p:
		# 	print(p.map(run_thread, self.population))
		for brain in self.population:
			snake = Snake(SIZE, False)
			while not snake.update_game():
				ins = snake.get_head_lidar()
				#print(ins)
				#exit(0)
				out = brain.run(ins)
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
			brain.fitness = snake.score + snake.size * 10 + (0 if snake.size == 3 else 500 - (snake.score/(snake.size - 3)))
		snake = Snake(SIZE, True)
		self.population.sort(key=get_fit, reverse=True)
		brain = self.population[0]
		while snake.update_graph():
			ins = snake.get_head_lidar()
			out = brain.run(ins)
			snake.direction = 0
			dirm = out[0]
			for i in range(4):
				if out[i] > dirm:
					dirm = out[i]
					snake.direction = i

	def reproduce(self):
		half_dna_length = len(self.population[0].dna) / 2
		for i in range(50, len(self.population)):
			father = self.population[random.randint(0, 50)]
			mother = self.population[random.randint(0, 50)]
			child = self.population[i]
			for pos in range(0, len(father.dna)):
				if pos < half_dna_length:
					child.dna[pos].weight = father.dna[pos].weight
				else:
					child.dna[pos].weight = mother.dna[pos].weight

			for i in range(1):
				child.dna[random.randint(0, (half_dna_length * 2) - 1)].weight = random.uniform(-1.0, 1)
