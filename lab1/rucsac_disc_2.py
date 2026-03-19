# varianta discreta in care retin doar ultimele doua linii din matrice at all times - trb modificata
n, c = [int(x) for x in input().split()]
valori = [int(x) for x in input().split()]
greutati = [int(x) for x in input().split()]

s = 0
dp = [[0]*(n+1)]*3 # 3 sau 2 girl cred ca 3?

for i in range(1, n + 1):
    for j in range(1, c+1):
        if greutati[i - 1] <= j:
            dp[1][j] = max(dp[0][j], dp[0][j - greutati[i - 1]] + valori[i - 1])
        else:
            dp[1][j] = dp[0][j]
    # reactualizarea matricei:
    for k in range(n+1):
        dp[0][k] = dp[1][k]

print(dp[len(dp)-1][len(dp[0])-1])