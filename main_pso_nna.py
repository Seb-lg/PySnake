import sys
sys.path.append("./venv/lib/python3.7/site-packages")
import matplotlib.pyplot as plt
from pso.pso import PSO
from nna.nna import NeuralNetwork


if __name__ == '__main__':
	plt.ion()
	pso = PSO(300, 1, [4, 8, 4], 1)
	best = NeuralNetwork(1, [4, 8, 4], 1)
	print(best.dna.__len__())
	data = []
	x = []
	y = []
	z = 0
	file = "1in_sine"
	with open("./pso/Data/" + file + ".txt", "r") as file1:
		for line in file1.readlines():
			f_list = [float(i) for i in line.split() if i.strip()]
			data.append(f_list)
			x.append(z)
			z += 1
			y.append(data[-1][-1])

	for i in range(200):
		pso.run_generation(data)

		for z in range(len(pso.population[0].best)):
			best.dna[z].weight = pso.population[0].best[z]

		plt.clf()
		ynna = []
		for elem in x:
			ynna.append(best.run(data[elem][:-1])[0])

		plt.title("MSE: " + pso.population[0].best_fitness.__str__())
		plt.plot(x, y)
		plt.plot(x, ynna)
		plt.pause(0.0001)
		plt.draw()

		pso.update_weights()

	print("MSE: " + pso.population[0].best_fitness.__str__())
	plt.savefig(file + ".png")
	while True:
		pass
