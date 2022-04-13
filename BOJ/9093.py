for _ in range (int(input())):
    arr = list(input().split())
    tmp = []
    for a in arr:
        tmp.append(a[::-1])
    print(' '.join(tmp))
