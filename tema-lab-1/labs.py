# labs : functiile implementate in laborator + overall logica evolutiei generatiilor de cromozomi
from chromosome import Chromosome as chr
import chromosome
import random as rnd
import output

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
        'generations': p_dim,                  # nr de cromozomi
        'start': dom[0],                      # capetele domeniului
        'end': dom[1],
        'a': param[0],                        # param functiei de gradul 2
        'b': param[1],
        'c': param[2],
        'precision': prec,                    # precizia cu care discretizam
        'crossover_probability': crossover_p, # probabilitatile
        'mutation_probability': mutation_p,
        'generation_count': steps,            # nr de etape ale chestiei
    }
    return data
# -------------------------------------------------------------------
# generarea de populatie, de cromozomi :3
def populate(config : dict) -> list[chr]:
    population: list[chr] = []

    # aflam lungimea
    chr.set_chromosome_length(config)

    # generam populatia noua
    for i in range(config["generations"]):
        chromosome_n : chr = chromosome.generate_chromosome(config)
        population.append(chromosome_n)

    # hello world
    return population

# fitness ul total al cromozomilor
def get_total_fitness(population : list[chr]) -> float:
    total_fitness = 0.0
    for chromosome in population:
        total_fitness += chromosome.fitness
    return total_fitness

def get_probabilities(population: list[chr], total_fitness: float) -> list[float]:
    if total_fitness == 0:
         return [1.0 / len(population)] * len(population)
         
    probabilities = []
    for chrom in population:
         prob = chrom.fitness / total_fitness
         probabilities.append(prob)
         
    return probabilities

# -------------------------------------------------------------------
# functiile din laborator :)

# random roulette generator + bin search pt noua noastra victima :D
def select_chromosome(population: list[chr], probabilities: list[float]) -> chr:
        
    # probabilitatile cumulate
    cumulative_probs = []
    current_sum = 0.0
    for p in probabilities:
        current_sum += p
        cumulative_probs.append(current_sum)
    
    # selectia propriu zisa
    u = rnd.random() # [0, 1)
        
    # cautare binara pt a gasi cromozomul (victima)
    stanga = 0
    dreapta = len(cumulative_probs) - 1
    index = 0
        
    while stanga <= dreapta:
        mijloc = (stanga + dreapta) // 2
        if cumulative_probs[mijloc] < u:
            stanga = mijloc + 1
        else:
            index = mijloc
            dreapta = mijloc - 1
                
    # protectie pentru erori de precizie float
    if index >= len(population):
        index = len(population) - 1
            
    return population[index], u

# imi fac eu cromozomul cu fitness si ce mai era da: va fi folosita si rescrisa la partea urmatoare so e mai usor sa apelam fct
def make_chromosome(bin_str: str, config: dict) -> chr:
    decimal_val = chromosome.get_decimal(bin_str, config)
    fit_val = chromosome.get_fitness(decimal_val, config)
    return chr(bin_str, decimal_val, fit_val)

# operatia de crossover cu tot cu alegerea 
def crossover(population: list[chr], config: dict, gen_count : int) -> list[chr]:
    crossover_prob = config['crossover_probability']
    participants_indices = []

    # alegem victimele (once again)
    for i, chrom in enumerate(population):
        u = rnd.random()
        if u < crossover_prob:
            participants_indices.append(i)

    # nu stiam sa handle uiesc daca am numar impar, dar o sa presupun ca nu mai face crossover
    if len(participants_indices) % 2 != 0:
        participants_indices.pop()

    # la primul pas printez tot
    if gen_count == 1:
        with open(output.filename, "a") as f:
            f.write(f"Probabilitatea de crossover: {crossover_prob}\n")
            for chromo in participants_indices:
                f.write(f"Alegem cromozomul {chromo+1}\n")

    binary_len = chr.binary_length  # luam lungimea

    # aici se intampla crossover ul real
    for i in range(0, len(participants_indices), 2):
        idx1 = participants_indices[i]
        idx2 = participants_indices[i+1]
    
        parent1 = population[idx1]
        parent2 = population[idx2]
    
        # alegem cut point ul - tot random
        cut_point = rnd.randint(1, binary_len - 1)

        child1 = parent1.binary[:cut_point] + parent2.binary[cut_point:]
        child2 = parent2.binary[:cut_point] + parent1.binary[cut_point:]

        if gen_count == 1:
            with open(output.filename, "a") as f:
                f.write(f"Facem crossover intre cromozomii {idx1+1} si {idx2+1} la punctul {cut_point}\n")
                f.write(f"Avem rezultatele: {child1} si {child2}\n\n")
    
        population[idx1] = make_chromosome(child1, config)
        population[idx2] = make_chromosome(child2, config)
    return population


# operatia de mutatie, unde se inverseaza bitul de la o pozitie random
def mutation(population: list[chr], config: dict, gen_count: int) -> list[chr]:
    # aceeasi logica: prob < => e ales
    mutation_prob = config['mutation_probability']
    binary_len = chr.binary_length
    
    if gen_count == 1:
        with open(output.filename, "a") as f:
            f.write(f"\nProbabilitatea de mutatie: {mutation_prob}\n")
    
    mutated_indices = []

    for i, chrom in enumerate(population):
        u = rnd.random()
        if u < mutation_prob:
            mutated_indices.append(i)
            # de unde se "rupe"
            pos = rnd.randint(0, binary_len - 1)
            
            bin_list = list(chrom.binary)
            bin_list[pos] = '1' if bin_list[pos] == '0' else '0'
            new_binary = "".join(bin_list)
            
            population[i] = make_chromosome(new_binary, config)
            
    if gen_count == 1:
        with open(output.filename, "a") as f:
            f.write("Au fost modificati cromozomii:\n")
            for idx in mutated_indices:
                f.write(f"{idx + 1}\n")
            
    return population


def mutation_updated(population: list[chr], config: dict, gen_count: int) -> list[chr]:
    # aceeasi logica: prob < => e ales
    mutation_prob = config['mutation_probability']
    binary_len = chr.binary_length

    if gen_count == 1:
        with open(output.filename, "a") as f:
            f.write(f"\nProbabilitatea de mutatie: {mutation_prob}\n")

    mutated_indices = []

    for i, chrom in enumerate(population):
        u = rnd.random()
        if u < mutation_prob:
            mutated_indices.append(i)
            # de unde se "rupe"
            pos = rnd.randint(0, binary_len - 1)

            bin_list = list(chrom.binary)
            new_bits = []

            if len(mutated_indices) == 1:
                print(f"mutation cromo {i+1}, de la valoarea {pos}:")
            for j in range(pos, binary_len):
                val = int(bin_list[j])
                if(len(mutated_indices) == 1):
                    print(f"{int(bin_list[j])}")
                if j > 0:
                    val += int(bin_list[j-1])
                    if len(mutated_indices) == 1:
                        print(f"{int(bin_list[j-1])}")
                if j < binary_len - 1:
                    val += int(bin_list[j+1])
                    if len(mutated_indices) == 1:
                        print(f"{int(bin_list[j+1])}")
                new_bits.append(str(val % 2))
                if len(mutated_indices) == 1:
                    print(f"suma lor e {val}, modificam in {str(val%2)}")


            bin_list[pos:binary_len] = new_bits
            new_binary = "".join(bin_list)
            if len(mutated_indices) == 1:
                print(f"noul cromo e {new_binary}")
            population[i] = make_chromosome(new_binary, config)

    if gen_count == 1:
        with open(output.filename, "a") as f:
            f.write("Au fost modificati cromozomii:\n")
            for idx in mutated_indices:
                f.write(f"{idx + 1}\n")

    return population

# la mutatie: in loc sa dau flip la bit, ma uit la maxim 3 valori (punctul de flip si vecinii ai)
# suma celor de langa % 2 facute in paralel

# -------------------------------------------------------------------
# partea a doua de cod: get_max_fitness si get_mean_fitness

def get_max_fitness(population: list[chr]) -> float:
    max = 0
    for chromo in population:
        if chromo.fitness > max:
            max = chromo.fitness
    return max

def get_mean_fitness(population: list[chr]) -> float:
    return (get_total_fitness(population)/len(population))