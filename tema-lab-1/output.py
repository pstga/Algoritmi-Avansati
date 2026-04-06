from chromosome import Chromosome
import chromosome

filename = "evolutie.txt"

# clear the file on run
with open(filename, "w") as f:
    pass

def print_init(population: list[Chromosome]):
    with open(filename, "a") as f:
        for i, chromosome in enumerate(population):
            f.write(f"{i+1}: {chromosome.binary}; x = {chromosome.decimal}; f(x) = {chromosome.fitness}\n")
        f.write("\n")
    return 0

def print_probs(probabilities: list[float]):
    with open(filename, "a") as f:
        f.write("Probabilitatile de selectie:\n")
        for i, prob in enumerate(probabilities):
            f.write(f"{i+1}: {prob}\n")
        f.write("\n")
    return 0

def print_intervals(probabilities: list[float]):
    with open(filename, "a") as f:
        f.write("Intervalele de selectie (probabilitatile cumulate):\n")
        current_sum = 0.0
        f.write(f"{current_sum:.6f}\n") # q_0
        for prob in probabilities:
            current_sum += prob
            f.write(f"{current_sum:.6f}\n") # q_i
        f.write("\n")
    return 0

def print_selected(selected_chromosome: chr, u: float, population: list[chr]):
    with open(filename, "a") as f:
        f.write(f"u= {u} => selectam cromozomul {population.index(selected_chromosome)+1}\n")
    return 0