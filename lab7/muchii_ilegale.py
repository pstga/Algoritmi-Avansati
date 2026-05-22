# ne folosim de prima problema; aflam pozitia unui punct fata de
# cercul circumscris al triunghiului format de celelalte 3 puncte
def pozitie_fata_de_cerc(A, B, C, P_test):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    xp, yp = P_test

    D = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

    if D == 0:
        return 0

    sq1 = x1 ** 2 + y1 ** 2
    sq2 = x2 ** 2 + y2 ** 2
    sq3 = x3 ** 2 + y3 ** 2

    X_num = sq1 * (y2 - y3) + sq2 * (y3 - y1) + sq3 * (y1 - y2)
    Y_num = sq1 * (x3 - x2) + sq2 * (x1 - x3) + sq3 * (x2 - x1)

    R_patrat_D_patrat = (X_num - x1 * D) ** 2 + (Y_num - y1 * D) ** 2

    dist_patrat_D_patrat = (X_num - xp * D) ** 2 + (Y_num - yp * D) ** 2

    if dist_patrat_D_patrat > R_patrat_D_patrat:
        return 'OUTSIDE'  # OUTSIDE
    elif dist_patrat_D_patrat < R_patrat_D_patrat:
        return 'INSIDE'  # INSIDE
    else:
        return 'BOUNDARY'  # BOUNDARY


def solve():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))

    # veridicam intai ac: daca d e strict in interior, atunci e ilegala si cealalta legala
    poz_D = pozitie_fata_de_cerc(A, B, C, D)
    if poz_D == 'INSIDE':  
        AC = "ILLEGAL"
    else:  # legala deci daca d se afla PE sau in afara cercului
        AC = "LEGAL"

    # verificam pozitia lui a fata de bcd cu aceeasi formula
    poz_A = pozitie_fata_de_cerc(B, C, D, A)
    if poz_A == 'INSIDE':
        BD = "ILLEGAL"
    else:  
        BD = "LEGAL"

    print(f"AC: {AC}")
    print(f"BD: {BD}")

if __name__ == "__main__":
    solve()