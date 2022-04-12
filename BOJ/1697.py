from collections import deque

def bfs(start):
    queue = deque([start])
    while queue:
        x = queue.popleft()
        if x == k:
            return visited[x]
        for n in (x-1, x+1, x*2):
            if 0<=n<=MAX and not visited[n]:
                visited[n] = visited[x]+1
                queue.append(n)

MAX = 100000
n, k = map(int, input().split())
visited = [0]*(MAX+1) # not MAX, MAX+1!! 방문한 노드가 아닌 시간 기록용
print(bfs(n))
