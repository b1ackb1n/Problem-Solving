n = int(input())
arr = list(map(int, input().split()))
tmp, height = [], []

for i in range(n-1):
    if arr[i]<arr[i+1]:
        tmp.append(arr[i])
        if i==n-2:
            if arr[n-1]>arr[i]:
                height.append(arr[n-1]-tmp[0])

    else:
        tmp.append(arr[i])
        height.append(tmp[-1]-tmp[0])
        tmp = []
        
print(max(height))