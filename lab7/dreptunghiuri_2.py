def binary_search_left(arr, x):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid
    return low


def solve():
    try:
        input_data = ""
        while True:
            line = input()
            if not line:
                break
            input_data += " " + line
    except EOFError:
        pass

    data = input_data.split()
    if not data:
        return

    idx = 0

    n = int(data[idx]);
    idx += 1

    left_set = set()  # x >= val  (a < 0, vertical)
    right_set = set()  # x <= val  (a > 0, vertical)
    bottom_set = set()  # y >= val  (b < 0, horizontal)
    top_set = set()  # y <= val  (b > 0, horizontal)

    for _ in range(n):
        a = int(data[idx]);
        idx += 1
        b = int(data[idx]);
        idx += 1
        c = int(data[idx]);
        idx += 1

        if a != 0:  # dreaptă verticală: ax + c <= 0
            val = -c / a
            if a > 0:
                right_set.add(val)  # x <= val
            else:
                left_set.add(val)  # x >= val
        else:  # dreaptă orizontală: by + c <= 0
            val = -c / b
            if b > 0:
                top_set.add(val)  # y <= val
            else:
                bottom_set.add(val)  # y >= val

    all_vert = sorted(list(left_set | right_set))
    all_horiz = sorted(list(bottom_set | top_set))

    m = int(data[idx]);
    idx += 1

    out = []
    for _ in range(m):
        xq = float(data[idx]);
        idx += 1
        yq = float(data[idx]);
        idx += 1

        # Căutare manuală în all_vert
        px = binary_search_left(all_vert, xq)
        if px < len(all_vert) and all_vert[px] == xq:
            out.append("NO")
            continue
        if px == 0 or px == len(all_vert):
            out.append("NO")
            continue

        x1 = all_vert[px - 1]  # imediat la stânga lui xq
        x2 = all_vert[px]  # imediat la dreapta lui xq

        if x1 not in left_set or x2 not in right_set:
            out.append("NO")
            continue

        # Căutare manuală în all_horiz
        py = binary_search_left(all_horiz, yq)
        if py < len(all_horiz) and all_horiz[py] == yq:
            out.append("NO")
            continue
        if py == 0 or py == len(all_horiz):
            out.append("NO")
            continue

        y1 = all_horiz[py - 1]
        y2 = all_horiz[py]

        if y1 not in bottom_set or y2 not in top_set:
            out.append("NO")
            continue

        area = (x2 - x1) * (y2 - y1)
        out.append(f"YES\n{area:.6f}")

    # Afișare normală cu print
    print('\n'.join(out))


if __name__ == "__main__":
    solve()