def orientare(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2


def is_on_segment(p, q, r):
    # punctul e sau nu pe segment
    if (r[0] <= max(p[0], q[0]) and r[0] >= min(p[0], q[0]) and
            r[1] <= max(p[1], q[1]) and r[1] >= min(p[1], q[1])):
        return True
    return False


def solve():
    n = int(input())
    polygon = []
    for _ in range(n):
        polygon.append(list(map(int, input().split())))

    m = int(input())
    for _ in range(m):
        point = list(map(int, input().split()))

        is_inside = True
        is_boundary = False
        initial_orientation = None

        for i in range(n):
            p1 = polygon[i]
            p2 = polygon[(i + 1) % n]

            orientation = orientare(p1, p2, point)

            if orientation == 0:
                if is_on_segment(p1, p2, point):
                    is_boundary = True
                    break
                else: # coliniar cu o latura dar nu e pe segment in convex e afara
                    is_inside = False
                    break

            if initial_orientation is None:
                initial_orientation = orientation
            elif orientation != initial_orientation:
                is_inside = False
                break

        if is_boundary:
            print("BOUNDARY")
        elif is_inside:
            print("INSIDE")
        else:
            print("OUTSIDE")


if __name__ == "__main__":
    solve()
    # for safety varianta naspa
    # ok aparent era rau oricum