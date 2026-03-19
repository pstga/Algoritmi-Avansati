# fac diferenta intre x-xa/xb-xa = y-ya/yb-ya si vad daca e 0, mai mica sau mai mare
def orientare(xp, yp, xq, yq, xr, yr):
    cross = (xq - xp) * (yr - yp) - (yq - yp) * (xr - xp)
    if cross > 0:
        return 'LEFT'
    elif cross < 0:
        return 'RIGHT'
    else:
        return 'TOUCH'

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        xp, yp, xq, yq, xr, yr = map(float, input().split())
        print(orientare(xp, yp, xq, yq, xr, yr))
