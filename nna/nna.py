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
		#print(len(self.layers))
		for i in range(len(self.layers) - 1):
			for current in self.layers[i]:
				for next in self.layers[i + 1]:
					link = Connection(current, next)
					current.next_link.append(link)
					next.prev_link.append(link)
					self.dna.append(link)

		for connection in self.dna:
			connection.weight = random.uniform(-1.0, 1.0)

	def run(self, input_data):
		for i in range(0, len(input_data)):
			self.layers[0][i].activated = input_data[i]

		#for layer in self.layers:
		#	for neuron in layer:
		#		neuron.total = 0.0

		for i in range(1, len(self.layers)):
			for neuron in self.layers[i]:
				#for prev in neuron.prev_link:
				#	neuron.total += prev.prev.activated * prev.weight
				neuron.activate()
		out = []
		for neuron in self.layers[-1]:
			# neuron.activate()
			out.append(neuron.activated)
		return out
