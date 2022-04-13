from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
arr = list(permutations(numbers, n))
cnt = []

for a in arr:
    tmp = 0
    for i in range (n-1):
        tmp += abs(a[i]-a[i+1])
    cnt.append(tmp)

print(max(cnt))
