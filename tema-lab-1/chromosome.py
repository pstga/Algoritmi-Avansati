# as muta totusi clasa aici ca e mai usor
import math
import random

class Chromosome:
    binary_len = 0
    def __init__(self, binary: str, decimal: float, fitness: float):
        self.binary = binary
        self.decimal = decimal
        self.fitness = fitness

    # log2[(b - a) * 10^p]
    def set_chromosome_length(data: dict) -> None:
        Chromosome.binary_length = math.ceil(
            math.log((data["end"] - data["start"]) * 10 ** data["precision"], 2))


# presupun ca i generez si p astia random ca nu a specificat nimeni nimic ??
def generate_chromosome(config: dict):
    # luam un nr random care se potriveste intervalului
    value: int = random.randint(0, 2 ** Chromosome.binary_length - 1)
    binary: str = get_binary(value)
    decimal: float = get_decimal(binary, config)
    fitness: float = get_fitness(decimal, config)
    return Chromosome(binary, decimal, fitness)

# umplem la stanga - am folosit functia din laborator :)
def get_binary(value: int) -> str:
    return bin(value)[2:].zfill(Chromosome.binary_length)

# bin(x) -> (b - a) / (2^l - 1) * dec(x) + a
def get_decimal(binary: str, config: dict) -> float:
    return round(
        int(binary, 2) * (config["domain_end"] - config["domain_start"]) / (2 ** Chromosome.binary_length - 1) +
        config["domain_start"], config["precision"])

# aplicam functia
def get_fitness(decimal: float, config: dict) -> float:
    return config["a"] * decimal * decimal + config["b"] * decimal + config["c"]