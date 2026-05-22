def orientare(O, A, B):
    return (A[0] - O[0]) * (B[1] - O[1]) - (A[1] - O[1]) * (B[0] - O[0])


def pe_segment(A, B, P):
    if orientare(A, B, P) != 0:
        return False
    return (min(A[0], B[0]) <= P[0] <= max(A[0], B[0]) and
            min(A[1], B[1]) <= P[1] <= max(A[1], B[1]))


def check_position(poligon, punct):
    n = len(poligon)
    if n < 3:
        return "OUTSIDE"
    if poligon[0][0] == punct[0] and poligon[0][1] == punct[1]:
        return "BOUNDARY"

    st = 1
    dr = n - 1
    while st < dr:
        mij = (st + dr + 1) // 2
        if orientare(poligon[0], poligon[mij], punct) >= 0:
            st = mij
        else:
            dr = mij - 1

    urmator = (st + 1) % n

    if (pe_segment(poligon[0], poligon[st], punct) or
            pe_segment(poligon[st], poligon[urmator], punct) or
            pe_segment(poligon[urmator], poligon[0], punct)):
        return "BOUNDARY"

    c1 = orientare(poligon[0], poligon[st], punct)
    c2 = orientare(poligon[st], poligon[urmator], punct)
    c3 = orientare(poligon[urmator], poligon[0], punct)

    if c1 >= 0 and c2 >= 0 and c3 >= 0:
        return "INSIDE"
    return "OUTSIDE"


def verificare_lenta(poligon, punct):
    n = len(poligon)
    for i in range(n):
        urmator = (i + 1) % n
        if pe_segment(poligon[i], poligon[urmator], punct):
            return "BOUNDARY"
        if orientare(poligon[i], poligon[urmator], punct) < 0:
            return "OUTSIDE"
    return "INSIDE"


def solve():
    n = int(input())
    poligon = []
    for _ in range(n):
        poligon.append(list(map(int, input().split())))

    m = int(input())
    for _ in range(m):
        interogare = list(map(int, input().split()))
        if n <= 100:
            print(verificare_lenta(poligon, interogare))
        else:
            print(check_position(poligon, interogare))


if __name__ == "__main__":
    solve()