import sys
sys.path.append("../")
sys.path.append("../venv/lib/python3.7/site-packages")
import matplotlib.pyplot as plt
from pso.pso import PSO
from nna.nna import NeuralNetwork

if __name__ == '__main__':
	plt.ion()
	pso = PSO(40, 1, [8, 16, 8], 1)
	best = NeuralNetwork(1, [8, 16, 8], 1)
	print(best.dna.__len__())
	data = []
	x = []
	y = []
	z = 0
	with open("../pso/Data/1in_linear.txt", "r") as file1:
		for line in file1.readlines():
			f_list = [float(i) for i in line.split() if i.strip()]
			data.append(f_list)
			#x.append(data[-1][0])
			x.append(z)
			z += 1
			y.append(data[-1][-1])

	for i in range(100):
		pso.run_generation(data)

		for z in range(len(pso.population[0].best)):
			best.dna[z].weight = pso.population[0].best[z]

		plt.clf()
		for brain in pso.population:
			ynna = []
			for elem in x:
				ynna.append(brain.neuralNetwork.run(data[elem][:-1])[0])
			#plt.plot(x, ynna)
		ynna = []
		for elem in x:
			ynna.append(best.run(data[elem][:-1])[0])

		plt.title("MSE: " + pso.population[0].best_fitness.__str__())
		plt.plot(x, y)
		plt.plot(x, ynna)
		plt.pause(0.0001)
		plt.draw()

		pso.update_weights()

	print(data[49][1])
	print(pso.population[0].neuralNetwork.run(data[49][:-1]))
	while True:
		pass
