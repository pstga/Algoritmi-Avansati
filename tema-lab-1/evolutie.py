import labs
from chromosome import Chromosome as chr

if __name__ == '__main__':
    data = {}
    data = labs.read_input()
    population: list[chr] = labs.generate_population(data)
    generations: list[list[chr]] = [population]
    gen_count: int = 1
    while gen_count < data["generations"]:
        # selection
        # crossover
        # mutation
        gen_count += 1


    print("Hello world!")
