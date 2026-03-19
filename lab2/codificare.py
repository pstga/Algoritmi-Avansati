import math as m

# functia de decodificare
def to(a, n, d, l):
    # aflu in ce interval de discretizare se afla (a + i*d)= nr =>> floor((nr-a)/d) si il transform in binar pe l biti
    idx = int((n - a) / d)
    return bin(idx)[2:].zfill(l)
    # transf in biti succes bagamiaspula

# functia de codificare
def fromm(a, n, d):
    # capatul din stanga al intervalului de discretizare (??)
    # transform nr din binar in zecimal si fac a * id
    nr = 0
    for i in range(0, len(n)):
        nr += (2**i)*int(n[len(n)-i-1])
    return a + nr*d

# calculul lungimii nr binar
def calc_l(a, b, p):
    return m.log(((b-a)*(10**p)), 2)

# calculul pasului de discretizare
def calc_d(b, a, l):
    return (b-a)/(2**l)


if __name__ == '__main__':
    a, b = map(int, input().split())
    p = int(input())
    steps = int(input())
    l = m.ceil(calc_l(a, b, p))
    d = calc_d(b, a, l)
    for _ in range(steps):
        task = input()
        if task == 'TO':
            res = to(a, float(input()), d, l)
            print(res)
        else:
            res = fromm(a, input(), d)
            print(res)