from neat.neatnna import NeatNeuralNetwork
from snake import *
from config import *


if __name__ == '__main__':
	graph = Snake(SIZE, True)
	champion = NeatNeuralNetwork(24, 4, 20)
	champion.load("best_457.nna")

	print("------------------------")
	for elem in champion.dna:
		print(elem.prev.next_link.index(elem))

	graph.clear()
	while graph.update_graph():
		ins = graph.get_head_lidar()
		out = champion.run(ins)

		dirm = out[0]
		dir = 0
		for i in range(4):
			if out[i] > dirm:
				dirm = out[i]
				dir = i
		newpos = None

		tmp = graph.snake[-1]
		if dir == right:
			newpos = [tmp[0] + 1, tmp[1]]
		elif dir == down:
			newpos = [tmp[0], tmp[1] + 1]
		elif dir == left:
			newpos = [tmp[0] - 1, tmp[1]]
		elif dir == up:
			newpos = [tmp[0], tmp[1] - 1]
		if not newpos in graph.snake:
			graph.direction = dir
