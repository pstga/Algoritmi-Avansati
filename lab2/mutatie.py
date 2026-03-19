l, k = map(int, input().split())
c = [x for x in input()]
switches = [int(x) for x in input().split()]
for x in switches:
    c[x] = str(int(not(int(c[x]))))
res = "".join(c)
print(res)