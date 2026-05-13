def orientare(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

if __name__ == '__main__':
    n = int(input())
    S = []

    for _ in range(n):
        x, y = map(int, input().split())
        S.append([x, y])

    if n < 3:
        print(n)
        for p in S:
            print(f"{p[0]} {p[1]}")
    else:
        start_idx = 0
        for i in range(1, n):
            if S[i][1] < S[start_idx][1] or (S[i][1] == S[start_idx][1] and S[i][0] < S[start_idx][0]):
                start_idx = i

        puncte_ordonate = S[start_idx:] + S[:start_idx]

        hull = []
        for p in puncte_ordonate:
            while len(hull) >= 2:
                if orientare(hull[-2], hull[-1], p) <= 0:
                    hull.pop()
                else:
                    break
            hull.append(p)

        while len(hull) >= 3:
            if orientare(hull[-2], hull[-1], hull[0]) <= 0:
                hull.pop()
            else:
                break

        print(len(hull))
        for point in hull:
            print(f"{point[0]} {point[1]}")