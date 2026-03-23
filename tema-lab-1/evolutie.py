# decodificarea cromozomului in raport cu domeniul de definitie
def decode(c, lo, hi, prec):
    return 1

# functia din cerinta
def f(a, b, c, ch):
    return (a*ch*ch) + (b*ch) + c

if __name__ == '__main__':
    # citesc toate datele bagami as pula in ele de date
    p_dim = int(input())                # dim pop - nr cromozomi
    lo, hi = map(int, input().split())  # dom de definitie f
    a, b, c = map(int, input().split()) # parametrii f
    prec = int(input())                 # precizia de discretizare
    crossover_p = int(input())          # prob de crossover
    mutation_p = int(input())           # prob de mutatie
    steps = int(input())                # nr de etape
    chromosomes = []
    # whatever these mean

    for _ in range(p_dim):
        c = input()
        ch = decode(c) # de intrebat daca pot scrie doar c = decode(c) desi schimba tipul din str in float
        chromosomes.append(ch)
        fc = f(a, b, c, ch) # aplic functia f pt a afla in pula mea functia
