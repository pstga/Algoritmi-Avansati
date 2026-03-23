from chromosome import Chromosome

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
# functiile din laborator :)

