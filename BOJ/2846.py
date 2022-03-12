N = int(input())
arr = list(map(int, input().split()))
tmp, height = [], []

for i in range(N-1):
    if arr[i]<arr[i+1]:
        tmp.append(arr[i])
        if i==N-2:
            if arr[N-1]>arr[i]:
                height.append(arr[N-1]-tmp[0])

    else:
        tmp.append(arr[i])
        num = tmp[-1]-tmp[0]
        height.append(num)
        tmp = []
        
print(max(height))
