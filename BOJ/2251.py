from collections import deque

answer = []
a, b, c = map(int, input().split())

queue = deque([(0,0)])

visited = [[0]*(b+1) for _ in range (a+1)]
visited[0][0] = 1

def pour(x,y):
    if not visited[x][y]:
        visited[x][y] = 1
        queue.append((x,y))

def bfs():  
    while queue:
        x, y = queue.popleft()
        z = c-x-y

        if x==0: answer.append(z)

        # a->b
        water = min(x, b-y)
        pour(x-water, y+water)
        # a->c
        water = min(x, c-z)
        pour(x-water, y)
        # b->a
        water = min(y, a-x)
        pour(x+water, y-water)
        # b->c
        water = min(y, c-z)
        pour(x, y-water)
        # c->a
        water = min(z, a-x)
        pour(x+water, y)
        # c->b
        water = min(z, b-y)
        pour(x, y+water)

bfs()
answer.sort()
print(*answer) # for i in sorted(answer): print(i, end=' ')
