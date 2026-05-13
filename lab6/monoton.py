def monotonie(coords):
    n = len(coords)
    if n < 3:
        return True

    turns = 0
    for i in range(n):
        prev_val = coords[i - 1]
        curr_val = coords[i]
        next_val = coords[(i + 1) % n] # cerculet la ultimul

        if curr_val == next_val: # aceeasi valoare => continuam nu conteaza
            continue

        j = (i + 1) % n
        while coords[j] == curr_val:
            j = (j + 1) % n
        next_val_distinct = coords[j]

        # s a intamplat ceva !
        if (curr_val > prev_val and curr_val > next_val_distinct) or \
                (curr_val < prev_val and curr_val < next_val_distinct):
            turns += 1

    # merg pe tot poligonul deci am 2 turn uri in "colturi" adica varfu de sus si cel de jos
    return turns <= 2


def solve():
    line1 = input().split()
    if not line1:
        return
    n = int(line1[0])

    points = []
    while len(points) < n:
        data = input().split()
        for i in range(0, len(data), 2):
            if len(points) < n:
                x = int(data[i])
                y = int(data[i + 1])
                points.append((x, y))

    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]

    is_x = monotonie(x_coords)
    is_y = monotonie(y_coords)

    print("YES" if is_x else "NO")
    print("YES" if is_y else "NO")


if __name__ == "__main__":
    solve()
    # and this is it kisses