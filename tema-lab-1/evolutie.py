# evolutie: main ul meu basically, doar l am numit evolutie initial inainte sa il impart pe mai multe fisiere :)
import labs
import output
import interface

from chromosome import Chromosome as chr

if __name__ == '__main__':
    data = {}
    data = labs.read_input()
    population: list[chr] = labs.populate(data)
    generations: list[list[chr]] = [population]
    gen_count: int = 1
    while gen_count < data["generation_count"]:
        # la 1 am caz special: printez tot ce apuc
        if gen_count == 1:
            # initializam populatia
            total_fitness = labs.get_total_fitness(population)
            probabilities = labs.get_probabilities(population, total_fitness)
            with open("evolutie.txt", "a") as f:
                f.write("Populatia initiala:\n")
            # print ul de discretizare, probabilitati si starea actuala a generatiei; acesti pasi trebuie facuti doar la inceput intrucat nr ramane neschimbat
            output.print_init(population)
            output.print_probs(probabilities)
            output.print_intervals(probabilities)
            with open("evolutie.txt", "a") as f:
                f.write("-----\n")

            # selectie
            new_population: list[chr] = []
            
            # selectie elitista: il salvez pe primul (current best), iar apoi ii aleg random (probabilistic) pe restul -1
            best_chromosome = max(population, key=lambda c: c.fitness)
            new_population.append(best_chromosome)
            for i in range(1, data["generations"]):
                selected_chromosome, u = labs.select_chromosome(population, probabilities)
                new_population.append(selected_chromosome)
                output.print_selected(selected_chromosome, u, new_population)
            with open("evolutie.txt", "a") as f:
                f.write("\n")
                f.write("Dupa selectie:\n")
            output.print_init(new_population)
            # actualizam new population
            total_fitness = labs.get_total_fitness(new_population)
            probabilities = labs.get_probabilities(new_population, total_fitness)

            # crossover
            new_population = labs.crossover(new_population, data, gen_count)
            total_fitness = labs.get_total_fitness(new_population)
            probabilities = labs.get_probabilities(new_population, total_fitness)
            with open("evolutie.txt", "a") as f:
                f.write("Dupa crossover:\n")
            output.print_init(new_population)


            # mutation
            new_population = labs.mutation(new_population, data, gen_count)
            total_fitness = labs.get_total_fitness(new_population)
            probabilities = labs.get_probabilities(new_population, total_fitness)
            with open("evolutie.txt", "a") as f:
                f.write("Dupa mutatie:\n")
            output.print_init(new_population)
            
            population = new_population
            generations.append(population)
            
        else:
            # aceiasi pasi fara initializarea referitoare la discretizare si fara asa de multe print-uri
            total_fitness = labs.get_total_fitness(population)
            probabilities = labs.get_probabilities(population, total_fitness)

            # selectie
            new_population: list[chr] = []
            
            # logica de elitism
            best_chromosome = max(population, key=lambda c: c.fitness)
            new_population.append(best_chromosome)
            
            for i in range(1, data["generations"]):
                selected_chromosome, u = labs.select_chromosome(population, probabilities)
                new_population.append(selected_chromosome)

            # crossover
            new_population = labs.crossover(new_population, data, gen_count)
            total_fitness = labs.get_total_fitness(new_population)
            probabilities = labs.get_probabilities(new_population, total_fitness)

            # mutation
            new_population = labs.mutation(new_population, data, gen_count)
            total_fitness = labs.get_total_fitness(new_population)
            probabilities = labs.get_probabilities(new_population, total_fitness)

            with open("evolutie.txt", "a") as f:
                f.write(f"Generatia {gen_count+1}: \n Max fitness: {labs.get_max_fitness(new_population)}"
                        f", mean fitness: {labs.get_mean_fitness(new_population)}\n")
            
            population = new_population
            # pastram generatia mea pentru a lucra pe ea la crearea urmatoarei
            generations.append(population)

        gen_count +=1

# plotarea graficului
interval : float = 0.05
interface.visualizer(data, generations, interval)