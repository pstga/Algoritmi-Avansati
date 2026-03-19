# are aditia: nu daca exista/care e o solutie optima, ci si cate solutii optime exista?
# nu am apucat s o termin ca s a terminat laboratorul lols
a, b = map(int, input.split())
n = int(input())
medici = []
temp = []
rez = []
lastHr = a
for _ in range(n):
    s, f = map(int, input.split())
    medici.append([s, f])

medici.sort(key=lambda x: x[0])
i = 1  # doamne ma simt asa de c++ astazi
while i <= n:
    while (medici[i][0] <= lastHr):
        temp.append(medici[i])
        i += 1
    temp.sort(key=lambda x: x[1], reverse=True)
    maybe = temp[0]
    if maybe[1] <= lastHr:
        print('nu am solutie')
        break
    else:
        rez.append(maybe)
        lastHr = maybe[1]

#------------------------
# EXPLICATIE 
# acoperire intervale; sa nu uit sa verific daca nu cumva nu am o solutie invalida
# le sortez dupa ora de inceput, salvez cea mai tzie ora a medicului 1 si apoi le iau pe urmatoarele
# care incep inainte sa se termine tura, si il aleg pe cel cu sfarsit cat mai la dreapta
# (aici verific daca am sau nu sol)