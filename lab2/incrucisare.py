if __name__ == '__main__' :
    l = int(input())
    c1 = input()
    c2 = input()
    i = int(input())
    print(c1[:i] + c2[i:])
    print(c2[:i] + c1[i:])