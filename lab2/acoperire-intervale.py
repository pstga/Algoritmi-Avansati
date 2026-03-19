if __name__ == '__main__':
    a, b = map(int, input().split())
    n = int(input())

    doctors = []
    res = []
    f = True
    last = a
    for _ in range(1, n+1):
        st, end = map(int, input().split())
        doctors.append([st, end, _])
    doctors.sort(key=lambda x: x[0])

    i = 0
    while last < b:
        best_end = -float('inf')
        best_index = -1
        while i < n and doctors[i][0] <= last:
            if doctors[i][1] > best_end:
                best_end = doctors[i][1]
                best_index = doctors[i][2]
            i += 1

        if best_end == -1 or best_end <= last:
            f = False
            break
        last = best_end
        res.append(best_index)

    if f == False:
        print(0)
    else:
        print(len(res))
        for doctor in res:
            print(doctor, end = ' ')