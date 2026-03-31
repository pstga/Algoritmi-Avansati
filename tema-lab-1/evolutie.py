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
            total_fitness = labs.get_total_fitness(population)
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
            total_fitness = labs.get_total_fitness(new_population)
            probabilities = labs.get_probabilities(new_population, total_fitness)

            # crossover
            new_population = labs.crossover(new_population, data, gen_count)
            print("Dupa crossover:")
            output.print_init(new_population)

            # mutation
            new_population = labs.mutation(new_population, data, gen_count)
            print("Dupa mutatie:")
            output.print_init(new_population)
            
            generations.append(population)
            
        else:
            total_fitness = labs.get_total_fitness(population)
            probabilities = labs.get_probabilities(population, total_fitness)

            # selectie
            new_population: list[chr] = []
            for i in range(data["generations"]):
                selected_chromosome, u = labs.select_chromosome(population, probabilities)
                new_population.append(selected_chromosome)

            # crossover
            new_population = labs.crossover(new_population, data, gen_count)

            # mutation
            new_population = labs.mutation(new_population, data, gen_count)

            print(f"Generatia {gen_count+1}: \n Max fitness: {labs.get_max_fitness(new_population)}"
                  f", mean fitness: {labs.get_mean_fitness(new_population)}")
            
            generations.append(new_population)

        gen_count +=1

