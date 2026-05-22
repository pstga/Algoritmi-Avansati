def orientare(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

def pe_segment(p, q, r):
    return (min(p[0], q[0]) <= r[0] <= max(p[0], q[0]) and 
            min(p[1], q[1]) <= r[1] <= max(p[1], q[1]))

def check_point_neconvex(poligon, n, pct):
    x_p, y_p = pct
    intersectii = 0

    for i in range(n):
        p1 = poligon[i]
        p2 = poligon[(i + 1) % n] 

        if orientare(p1, p2, pct) == 0 and pe_segment(p1, p2, pct):
            return "BOUNDARY"

        if p1[1] > p2[1]:
            p1, p2 = p2, p1

        if p1[1] <= y_p < p2[1]:
            if orientare(p1, p2, pct) > 0:
                intersectii += 1

    if intersectii % 2 == 1:
        return "INSIDE"
    else:
        return "OUTSIDE"

def solve():
    n = int(input())
    poligon = []
    for _ in range(n):
        poligon.append(list(map(int, input().split())))

    m = int(input())
    for _ in range(m):
        pct = list(map(int, input().split()))
        print(check_point_neconvex(poligon, n, pct))

if __name__ == "__main__":
    solve()