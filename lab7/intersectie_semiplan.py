if __name__ == "__main__":
    n = int(input())

    x_min = float('-inf')
    x_max = float('inf')
    y_min = float('-inf')
    y_max = float('inf')

    for _ in range(n):
        # luam ecuatia
        a, b, c = map(int, input().split())

        # dreapta verticala
        if a != 0:
            valoare = -c / a  # bound ul pentru x pentru semiplan + update
            if a > 0:
                x_max = min(x_max, valoare)
            else:
                x_min = max(x_min, valoare)
        # orizontala
        else:
            valoare = -c / b  # bound y + update
            if b > 0:
                y_max = min(y_max, valoare)
            else:
                y_min = max(y_min, valoare)

    if x_min > x_max or y_min > y_max:
        print("VOID")
    # daca toate limitele au valori finite inseamna ca intersectia e bounded
    elif (x_min != float('-inf') and x_max != float('inf') and
          y_min != float('-inf') and y_max != float('inf')):
        print("BOUNDED")
    else:
        print("UNBOUNDED")