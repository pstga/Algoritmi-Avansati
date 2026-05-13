def orientare(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

def este_pe_segment(p, q, r):
    return (min(p[0], q[0]) <= r[0] <= max(p[0], q[0]) and min(p[1], q[1]) <= r[1] <= max(p[1], q[1]))

def check_point(poligon, n, pct):
    p0 = poligon[0]

    # e in afara celui mai din stg unghi => out direct
    if orientare(p0, poligon[1], pct) < 0 or orientare(p0, poligon[n - 1], pct) > 0:
        return "OUTSIDE"

    # daca nu cumva e pe vreuna din laturile ultimului unghi
    cp_prima = orientare(p0, poligon[1], pct)
    if cp_prima == 0:
        return "BOUNDARY" if este_pe_segment(p0, poligon[1], pct) else "OUTSIDE"

    cp_ultima = orientare(p0, poligon[n - 1], pct)
    if cp_ultima == 0:
        return "BOUNDARY" if este_pe_segment(p0, poligon[n - 1], pct) else "OUTSIDE"

    # incepem cautarea binara sa vedem in ce "triunghi" ma aflu :)
    st = 1
    dr = n - 2
    idx = 1

    while st <= dr:
        m = (st + dr) // 2
        if orientare(p0, poligon[m], pct) >= 0:
            idx = m
            st = m + 1
        else:
            dr = m - 1

    # orientarea fata de latura gasita
    rez = orientare(poligon[idx], poligon[idx + 1], pct)

    if rez > 0:
        return "INSIDE"
    elif rez == 0:
        return "BOUNDARY"
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
        print(check_point(poligon, n, pct))

if __name__ == "__main__":
    solve()