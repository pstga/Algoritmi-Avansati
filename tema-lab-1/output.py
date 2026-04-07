# output: toate functiile de print in fisiere pentru prima respectiv urmatoarele generatii
from chromosome import Chromosome
import chromosome

filename = "evolutie.txt"

# clear la inceput pt clean output
with open(filename, "w") as f:
    pass

# print-ul populatiei in generatia initiala
def print_init(population: list[Chromosome]):
    with open(filename, "a") as f:
        for i, chromosome in enumerate(population):
            f.write(f"{i+1}: {chromosome.binary}; x = {chromosome.decimal}; f(x) = {chromosome.fitness}\n")
        f.write("\n")
    return 0

# print-ul probabilitatior de la pasul 1
def print_probs(probabilities: list[float]):
    with open(filename, "a") as f:
        f.write("Probabilitatile de selectie:\n")
        for i, prob in enumerate(probabilities):
            f.write(f"{i+1}: {prob}\n")
        f.write("\n")
    return 0

# intervalele de discretizare
def print_intervals(probabilities: list[float]):
    with open(filename, "a") as f:
        f.write("Intervalele de selectie (probabilitatile cumulate):\n")
        current_sum = 0.0
        f.write(f"{current_sum:.6f}\n")
        for prob in probabilities:
            current_sum += prob
            f.write(f"{current_sum:.6f}\n")
        f.write("\n")
    return 0

# cromozomii selectati in urma procesului: evidentiare
def print_selected(selected_chromosome: chr, u: float, population: list[chr]):
    with open(filename, "a") as f:
        f.write(f"u= {u} => selectam cromozomul {population.index(selected_chromosome)+1}\n")
    return 0