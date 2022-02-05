n = int(input())
arr = list(map(int, input().split()))

length=[]
road=[]
for i in range (len(arr)-1):
    if arr[i]+1 < arr[i+1]:
        road.append(arr[i])
        if i+1 == len(arr)-1:
            road.append(arr[i+1])
            length.append(road[-1]-road[0])
    elif len(road)!=0 and arr[i]+1>=arr[i+1]:
        road.append(arr[i])
        length.append(road[-1]-road[0])
        road = []

if len(length)!=0:
    print(max(length))
else:
    print(0)
