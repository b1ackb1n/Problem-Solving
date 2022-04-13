from itertools import product

T = int(input())
numbers = [1, 2, 3]
for _ in range (T):
    n = int(input())
    cnt = 0
    for i in range (1, n+1):
        case = list(map(sum, product(numbers, repeat=i)))
        cnt += case.count(n)
    print(cnt)
