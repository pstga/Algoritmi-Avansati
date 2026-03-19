def directie(x1, y1, x2, y2, x3, y3):
    cross = (x2-x1)*(y3-y2) - (y2-y1)*(x3-x2)
    if cross > 0:
        return 'stanga'
    elif cross < 0:
        return 'dreapta'
    else:
        return 'drept'

if __name__ == '__main__':
    n = int(input())
    puncte = []
    viraje = [0, 0, 0] # stanga, drepata, ramane la fel
    for _ in range(n):
        x, y = map(int, input().split())
        puncte.append([x, y])
    puncte.append(puncte[0])

    x1, y1 = puncte[0][0], puncte[0][1]
    for i in range(1, len(puncte)):
        x2, y2 = puncte[i][0], puncte[i][1]
        try:
            x3, y3 = puncte[i+1][0], puncte[i+1][1]
        except:
            break
        viraj = directie(x1, y1, x2, y2, x3, y3)
        if viraj == 'stanga':
            viraje[0] += 1
        elif viraj == 'dreapta':
            viraje[1] += 1
        else:
            viraje[2] += 1
        x1, y1 = x2, y2

    print(viraje[0], viraje[1], viraje[2])


