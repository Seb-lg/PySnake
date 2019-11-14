from neat.neatgeneration import Generation

if __name__ == '__main__':
	gen = Generation(1000)
	age = 0
	max = 0
	while True:
		print(age, gen.population[0].fitness)
		# print("--", gen.population[0].neurons.__len__(), gen.population[0].dna.__len__())
		#print(gen.population)
		gen.run_generation()
		if gen.population[0].fitness > max:
			max = gen.population[0].fitness
			gen.population[0].save("best_" + str(age) + ".nna")
		gen.reproduce()
		age += 1
