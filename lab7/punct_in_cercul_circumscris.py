def check_circumcerc_exact(A, B, C, puncte_test):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    # aflam centrul cercului circumscris
    D = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

    if D == 0:
        return

    sq1 = x1 ** 2 + y1 ** 2
    sq2 = x2 ** 2 + y2 ** 2
    sq3 = x3 ** 2 + y3 ** 2

    X_num = sq1 * (y2 - y3) + sq2 * (y3 - y1) + sq3 * (y1 - y2)
    Y_num = sq1 * (x3 - x2) + sq2 * (x1 - x3) + sq3 * (x2 - x1)

    # aflam si raza
    R_patrat_D_patrat = (X_num - x1 * D) ** 2 + (Y_num - y1 * D) ** 2

    for x, y in puncte_test:
        dist_patrat_D_patrat = (X_num - x * D) ** 2 + (Y_num - y * D) ** 2

        if dist_patrat_D_patrat > R_patrat_D_patrat:
            print('OUTSIDE')
        elif dist_patrat_D_patrat < R_patrat_D_patrat:
            print('INSIDE')
        else:
            print('BOUNDARY')


if __name__ == '__main__':
    triunghi = []
    for _ in range(3):
        x, y = map(int, input().split())
        triunghi.append((x, y))

    n = int(input())
    puncte_test = []
    for _ in range(n):
        x, y = map(int, input().split())
        puncte_test.append((x, y))

    check_circumcerc_exact(triunghi[0], triunghi[1], triunghi[2], puncte_test)