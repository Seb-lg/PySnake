from pso.pso import PSO

if __name__ == '__main__':
	pso = PSO(200, 2, [4, 4, 4], 1)

	data = []
	with open("/home/seb/PySnake/pso/Data/2in_complex.txt", "r") as file1:
		for line in file1.readlines():
			f_list = [float(i) for i in line.split('\t') if i.strip()]
			data.append(f_list)
	for i in range(200):
		pso.run_generation(data)
		pso.update_weights()
		print(pso.population[0].best)
		print(pso.population[0].best_fitness)
		print(pso.population[-1].best_fitness)
		print("")

	print(data[49][1])
	print(pso.population[0].neuralNetwork.run(data[49][:-1]))
