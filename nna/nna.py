import random

from nna.node import Node
from nna.connection import Connection


class NeuralNetwork(object):
	def __init__(self, input, hiddenlayer, output):
		self.fitness = 0
		self.layers = []
		self.dna = []

		# Setting Nodes
		tmp = []
		for i in range(0, input):
			tmp.append(Node())
		self.layers.append(tmp)

		for layer in hiddenlayer:
			tmp = []
			for i in range(0, layer):
				tmp.append(Node())
			self.layers.append(tmp)

		tmp = []
		for i in range(0, output):
			tmp.append(Node())
		self.layers.append(tmp)


		# Setting Connections
		for i in range(len(self.layers) - 1):
			for current in self.layers[i]:
				for next in self.layers[i + 1]:
					link = Connection(current, next)
					current.next_link.append(link)
					next.prev_link.append(link)
					self.dna.append(link)

		#randomise weight
		for connection in self.dna:
			connection.weight = random.uniform(-1.0, 1.0)

	def run(self, input_data):
		#set input data in the neural network
		for i in range(0, len(input_data)):
			self.layers[0][i].activated = input_data[i]

		#run the neural network
		for i in range(1, len(self.layers)):
			for neuron in self.layers[i]:
				neuron.activate()

		#return the out put of the neural network
		out = []
		for neuron in self.layers[-1]:
			out.append(neuron.activated)
		return out
