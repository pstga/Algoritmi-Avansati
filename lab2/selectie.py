def fitness(x, a, b, ch):
    return a*(x**2) + b*x + ch

if __name__ == '__main__' :
    a, b, c = map(int, input().split())
    n = int(input())
    chromos = [float(x) for x in input().split()]
    s_partiale = [fitness(x, a, b, c) for x in chromos]
    fitsum = sum(s_partiale)
    sum = 0.0
    print(0.0)
    for fit in s_partiale:
        sum += fit
        res = sum/fitsum
        print(res)