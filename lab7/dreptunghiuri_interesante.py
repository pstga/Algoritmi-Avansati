from bisect import bisect_left, bisect_right

n = int(input())

left_set = set()   # x >= val  vert
right_set = set()  # x <= val
bottom_set = set() # y >= val  horiz
top_set = set()    # y <= val

for _ in range(n):
    a, b, c = map(int, input().split())

    if a != 0:  # vert
        val = -c / a
        if a > 0:
            right_set.add(val)  # x <= val
        else:
            left_set.add(val)   # x >= val
    else:       # horiz
        val = -c / b
        if b > 0:
            top_set.add(val)    # y <= val
        else:
            bottom_set.add(val) # y >= val

left_list = sorted(left_set)
right_list = sorted(right_set)
bottom_list = sorted(bottom_set)
top_list = sorted(top_set)

m = int(input())

for _ in range(m):
    xq, yq = map(float, input().split())

    eps = 1e-9

    px1 = bisect_left(left_list, xq - eps)
    if px1 == 0:
        print("NO")
        continue
    x1 = left_list[px1 - 1]

    px2 = bisect_right(right_list, xq + eps)
    if px2 == len(right_list):
        print("NO")
        continue
    x2 = right_list[px2]

    if x1 >= x2:
        print("NO")
        continue

    py1 = bisect_left(bottom_list, yq - eps)
    if py1 == 0:
        print("NO")
        continue
    y1 = bottom_list[py1 - 1]

    py2 = bisect_right(top_list, yq + eps)
    if py2 == len(top_list):
        print("NO")
        continue
    y2 = top_list[py2]

    if y1 >= y2:
        print("NO")
        continue

    # gata aria gata problema SPER CA NU MAI POT
    area = (x2 - x1) * (y2 - y1)
    print("YES")
    print(f"{area:.6f}")