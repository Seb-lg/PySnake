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
		self.total = 0
		for connection in self.prev_link:
			self.total += connection.prev.activated * connection.weight
		self.activated = sigmoid(self.total)
