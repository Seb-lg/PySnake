import math


def sigmoid(x):
	return (1 / (1 + math.exp(-x))) * 2 - 1


class Node(object):

	def __init__(self):
		self.total = 0.0
		self.activated = 0.0

		self.prev_link = []
		self.next_link = []

	def activate(self):
		#set the sactivated value of a neuron
		self.total = 0.0
		for previous in self.prev_link:
			self.total += previous.prev.activated * previous.weight
		self.activated = sigmoid(self.total)
