from chromosome import Chromosome as chr
import random as rnd

# -------------------------------------------------------------------
# get input din txt pentru rezolvarea problemei
def read_input() -> dict:
    with open("input.txt", "r") as f:
        p_dim = int(f.readline())
        dom = [int(v) for v in f.readline().split()]
        param = [int(v) for v in f.readline().split()]
        prec = int(f.readline())
        crossover_p = float(f.readline())
        mutation_p = float(f.readline())
        steps = int(f.readline())
    data = {
        'population': p_dim,                  # nr de cromozomi
        'start': dom[0],                      # capetele domeniului
        'end': dom[1],
        'a': param[0],                        # param functiei de gradul 2
        'b': param[1],
        'c': param[2],
        'precision': prec,                    # precizia cu care discretizam
        'crossover_probability': crossover_p, # probabilitatile
        'mutation_probability': mutation_p,
        'generation_count': steps,            # nr de etape ale chestiei
        "maximize": True                      # cum arata bolta :)))
    }

    if data["a"] > 0: # avem maxim sau minim?
        data["maximize"] = False

    return data
# -------------------------------------------------------------------
# generarea de populatie, de cromozomi :3

def populate(config : dict) -> list[chr.Chromosome]:
    population: list[chr.Chromosome] = []

    # aflam lungimea
    chr.set_chromosome_length(config)

    # generam populatia noua
    for i in range(config["population"]):
        chromosome : chr.Chromosome = chr.generate_chromosome(config)
        population.append(chromosome)

    # hello world
    return population

# fitness ul total al cromozomilor
def get_population_fitness(pop : list[chr.Chromosome]) -> float:
    total_fitness = 0.0
    for chromosome in pop:
        total_fitness += chromosome.fitness
    return total_fitness

# -------------------------------------------------------------------
# functiile din laborator :)

# alegem urmatoarele victime
def generator(population: list[chr], data : dict) -> chr:
    fitness = [chrom.fitness for chrom in population]

    if data['maximize'] is True:
        min_f = min(fitness)
        if min_f < 0:
            shf = [f - min_f + 0.001 for f in fitness]
        else:
            shf = fitness
    else:
        max_f = max(fitness)
        shf = [max_f - f + 0.001 for f in fitness]
    total = sum(shf)
    val = rnd.uniform(0, 1)
    cummulative = 0

    for i, chromosome in enumerate(population):
        cummulative += shf[i] / total
        if cummulative >= val:
            return chromosome
    return population[-1]

def selection(config: dict, population: list[chr]) -> list[chr]:

    new_population: list[chr] = []

    for i in range(config["population_size"]):
        selected_chromosome = generator(population, config)
        new_population.append(selected_chromosome)

    return new_population

def mutation(config : dict, population : list[chr]) -> list[chr]:
    new_population : list[chr] = population.copy()

    for i in range(len(new_population)):
        u : float = rnd.uniform(0, 1)
        if u < config["mutation_probability"]:
            bit : int = rnd.randint(0, rnd.Chromosome.binary_length - 1)
            binary : str = new_population[i].binary
            new_bit : int = 1 - int(binary[bit])
            new_binary : str = binary[:bit] + str(new_bit) + binary[(bit+1):]
            new_decimal : float = chr.get_decimal(new_binary, config)
            new_fitness : float = chr.get_fitness(new_decimal, config)
            new_population[i] = chr.Chromosome(new_binary, new_decimal, new_fitness)

    return new_population

def get_crossover_list(config : dict, population : list[chr]) -> list[int]:
    return 1

def crossover():
    return 1

