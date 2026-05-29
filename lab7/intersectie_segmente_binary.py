from bisect import bisect_left, bisect_right

def rezolva_intersectii():
    n = int(input())

    evenimente = []

    for _ in range(n):
        date = list(map(int, input().split()))
        x1, y1, x2, y2 = date[0], date[1], date[2], date[3]

        if y1 == y2:  # segment orizontal
            x_st, x_dr = min(x1, x2), max(x1, x2)
            # 0 -incepe o linie orizontala
            evenimente.append((x_st, 0, y1))
            # 2 - se termina o linie orizontala
            evenimente.append((x_dr, 2, y1))
        else:  # segment vertical
            y_j, y_s = min(y1, y2), max(y1, y2)
            # 1 - linia verticala care verifica intersectiile
            evenimente.append((x1, 1, y_j, y_s))

    # sortam toate evenimentele dupa coordonata x
    evenimente.sort()

    active_y = []
    total_intersectii = 0

    for ev in evenimente:
        if ev[1] == 0:
            # incepe o linie orizontala, o punem in lista mentinand ordinea
            y_val = ev[2]
            pos = bisect_left(active_y, y_val)
            active_y.insert(pos, y_val)

        elif ev[1] == 2:
            # se termina linia orizontala, o scoatem din lista de linii active
            y_val = ev[2]
            pos = bisect_left(active_y, y_val)
            if pos < len(active_y) and active_y[pos] == y_val:
                active_y.pop(pos)

        elif ev[1] == 1:
            # avem o linie verticala, cautam rapid cate orizontale o intersecteaza
            y_j, y_s = ev[2], ev[3]
            st = bisect_left(active_y, y_j)
            dr = bisect_right(active_y, y_s)
            # compl logaritm
            total_intersectii += (dr - st)

    print(total_intersectii)


if __name__ == '__main__':
    rezolva_intersectii()