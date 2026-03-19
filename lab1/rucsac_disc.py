# intai cu matrice, apoi modificam sa retinem doar ultimele 2 linii

# n obiecte C capacitate maxima
# valoare v greutate g citite pe linii
n, c = [int(x) for x in input().split()]
valori = [int(x) for x in input().split()]
greutati = [int(x) for x in input().split()]

s = 0
dp = [[0 for _ in range(c + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, c + 1):
        if greutati[i - 1] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - greutati[i - 1]] + valori[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[len(dp)-1][len(dp[0])-1])