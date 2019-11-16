from pso.pso import PSO

if __name__ == '__main__':
	pso = PSO(200)

	data = []
	with open("/home/seb/PySnake/pso/Data/2in_complex.txt", "r") as file1:
		for line in file1.readlines():
			f_list = [float(i) for i in line.split('\t') if i.strip()]
			data.append(f_list)
	while True:
		pso.run_generation(data)
		pso.update_weights()
		print(pso.population[0].score)
		print(pso.population[-1].score)
		print("")
