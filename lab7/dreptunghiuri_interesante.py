# prelucrare pt punct
def rezolva_punct(Q, bariere_st, bariere_dr, bariere_jos, bariere_sus, toate_semiplanele):
    xq, yq = Q

    # cea mai apropiata valoare din stanga
    x_st = float('-inf')
    for v in bariere_st:
        if v < xq:
            x_st = max(x_st, v)

    # -''- dreapta
    x_dr = float('inf')
    for v in bariere_dr:
        if v > xq:
            x_dr = min(x_dr, v)

    # -''- jos
    y_jos = float('-inf')
    for h in bariere_jos:
        if h < yq:
            y_jos = max(y_jos, h)

    # -''- sus
    y_sus = float('inf')
    for h in bariere_sus:
        if h > yq:
            y_sus = min(y_sus, h)

    # valoare infinita => unbounded => nu avem dreptunghi
    if x_st == float('-inf') or x_dr == float('inf') or y_jos == float('-inf') or y_sus == float('inf'):
        return "NO", None

    # verificam daca dreptunghiul exista (nu trece alta bariera prin el, etc)
    for tip, val in toate_semiplanele:
        if tip == 'ST' and val > x_st and val < x_dr:
            if val > xq:
                return "NO", None
        if tip == 'DR' and val < x_dr and val > x_st:
            if val < xq:
                return "NO", None
        if tip == 'JOS' and val > y_jos and val < y_sus:
            if val > yq:
                return "NO", None
        if tip == 'SUS' and val < y_sus and val > y_jos:
            if val < yq:
                return "NO", None

    # calculam aria pentru un dreptunghi care chiar exista !!!
    arie = (x_dr - x_st) * (y_sus - y_jos)
    return "YES", arie


def solve():
    n = int(input())

    # ne facem lista de bound uri pe toate partile
    bariere_st = []
    bariere_dr = []
    bariere_jos = []
    bariere_sus = []
    toate_semiplanele = []

    # ne cautam bound urile in fiecare semiplan oferit
    for _ in range(n):
        a, b, c = map(int, input().split())
        if a != 0:
            val = -c / a
            if a > 0:  # bariera dreapta
                bariere_dr.append(val)
                toate_semiplanele.append(('DR', val))
            else:  # bariera stanga
                bariere_st.append(val)
                toate_semiplanele.append(('ST', val))
        elif b != 0:
            val = -c / b
            if b > 0:  # bariera sus
                bariere_sus.append(val)
                toate_semiplanele.append(('SUS', val))
            else:  # bariera jos
                bariere_jos.append(val)
                toate_semiplanele.append(('JOS', val))

    # incepem sa citim punctele
    m = int(input())
    for _ in range(m):
        xq, yq = map(float, input().split())
        status, aria_minima = rezolva_punct((xq, yq), bariere_st, bariere_dr, bariere_jos, bariere_sus, toate_semiplanele)

        print(status)
        if status == "YES":
            print(f"{aria_minima:.6f}")


if __name__ == "__main__":
    solve()

# are 50% check conditii ca nu mai stiu daca s bune (sigur nu sunt daca are 50%)