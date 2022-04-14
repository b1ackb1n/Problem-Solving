n = int(input())
table, rank = [], []
for _ in range (n):
    w, h = map(int, input().split(' '))
    table.append((w,h))

for i in range (n):
    k=0
    for j in range (n):
        if table[i][0]<table[j][0] and table[i][1]<table[j][1]:
            k+=1
    rank.append(k+1)
        
print(*rank)
