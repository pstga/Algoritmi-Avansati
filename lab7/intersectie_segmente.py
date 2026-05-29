def rezolva_intersectii():
    n = int(input())

    segmente = []

    for _ in range(n):
        date = list(map(int, input().split()))
        x1, y1, x2, y2 = date[0], date[1], date[2], date[3]

        # segment orizontal
        if y1 == y2:
            x_inceput = min(x1, x2)
            x_sfarsit = max(x1, x2)
            y_pozitie = y1

            # punem cand incepe si cand se termina
            segmente.append((x_inceput, 0, y_pozitie)) # tipul 0 este inceput, tipul 2 este final de segment
            segmente.append((x_sfarsit, 2, y_pozitie))

        # segment vertical
        else:
            x_pozitie = x1
            y_jos = min(y1, y2)
            y_sus = max(y1, y2)

            # forma de segment vertical pt diferentiere
            segmente.append((x_pozitie, 1, y_jos, y_sus))

    # sortam segmentele dupa coordonata x (de aia am forme diferite de memorare la memorarea segmentelor)
    segmente.sort()

    # inaltimile y ale segmentelor + cnt
    linii_orizontale_active = []
    total_intersectii = 0

    for ev in segmente:
        tip_segment = ev[1]

        if tip_segment == 0:
            # inceput de linie orizontala
            y_pozitie = ev[2]
            linii_orizontale_active.append(y_pozitie)

        elif tip_segment == 2:
            # final linie orizontala => nu ma mai intereseaza => la revedere
            y_pozitie = ev[2]
            linii_orizontale_active.remove(y_pozitie)

        elif tip_segment == 1:
            # pastrez unde e linia mea verticala si vad de cate ori trece printr o orizontala
            y_jos = ev[2]
            y_sus = ev[3]

            # luam pe rand fiecare alt y si vad daca se intersecteaza sau nu
            for y_activ in linii_orizontale_active:
                if y_jos <= y_activ <= y_sus:
                    total_intersectii += 1

    print(total_intersectii)

if __name__ == '__main__':
    rezolva_intersectii()