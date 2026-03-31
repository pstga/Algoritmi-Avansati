from chromosome import Chromosome
import chromosome

def print_init(population: list[Chromosome]):
    for i, chromosome in enumerate(population):
        print(f"{i+1}: {chromosome.binary}; x = {chromosome.decimal}; f(x) = {chromosome.fitness}")
    print()
    return 0

def print_probs(probabilities: list[float]):
    print("Probabilitatile de selectie:")
    for i, prob in enumerate(probabilities):
        print(f"{i+1}: {prob}")
    print()
    return 0

def print_intervals(probabilities: list[float]):
    print("Intervalele de selectie (probabilitatile cumulate):")
    current_sum = 0.0
    print(f"{current_sum:.6f}") # q_0
    for prob in probabilities:
        current_sum += prob
        print(f"{current_sum:.6f}") # q_i
    print()
    return 0

def print_selected(selected_chromosome: chr, u: float, population: list[chr]):
    print(f"u= {u} => selectam cromozomul {population.index(selected_chromosome)+1}")
    return 0