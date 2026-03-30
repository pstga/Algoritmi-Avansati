import labs
import output
from chromosome import Chromosome as chr

if __name__ == '__main__':
    data = {}
    data = labs.read_input()
    population: list[chr] = labs.populate(data)
    generations: list[list[chr]] = [population]
    gen_count: int = 1
    while gen_count < data["generations"]:
        # la 1 am caz special: printez tot ce apuc
        if gen_count == 1:
            total_fitness = labs.get_population_fitness(population)
            probabilities = labs.get_probabilities(population, total_fitness)
            print("Populatia initiala:")
            output.print_init(population)
            output.print_probs(probabilities)
            output.print_intervals(probabilities)
            print("-----")

            # selectie
            new_population: list[chr] = []
            for i in range(data["generations"]):
                selected_chromosome, u = labs.select_chromosome(population, probabilities)
                new_population.append(selected_chromosome)
                output.print_selected(selected_chromosome, u, new_population)
            print()
            print("Dupa selectie:")
            output.print_init(new_population)
            total_fitness = labs.get_population_fitness(new_population)
            probabilities = labs.get_probabilities(new_population, total_fitness)

            # crossover
            new_population = labs.crossover(new_population, data, gen_count)
            print("Dupa crossover:")
            output.print_init(new_population)
            total_fitness = labs.get_population_fitness(new_population)
            probabilities = labs.get_probabilities(new_population, total_fitness)

            # mutation

            
        else:
            print("restul generatiilor")
            # doar ce mi zicea acl

        # next --->
        gen_count +=1

