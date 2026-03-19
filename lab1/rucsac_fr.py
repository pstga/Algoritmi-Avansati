# rucsac fractionar
n, gmax = [int(x) for x in input().split()]
valori = [int(x) for x in input().split()]
greutati = [int(x) for x in input().split()]
obj = []
for i in range(n):
    raport = valori[i] / greutati[i]
    obj.append([greutati[i], valori[i], raport])

obj.sort(key=lambda x: x[2], reverse=True)

s = 0
val = 0.0
for w, v, r in obj:
    if s + w > gmax:
        dif = gmax-s
        val += dif*r
        break
    else:
        s += w
        val += v

print(val)