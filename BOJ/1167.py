from collections import deque

graph = {}
V = int(input())
for _ in range (V): # 트리 생성
    n = list(map(int, input().split(' ')))
    for i in range (1, len(n)-2, 2):
        if n[0] not in graph:
            graph[n[0]] = [(n[i], n[i+1])]
        else:
            graph[n[0]].append((n[i], n[i+1]))

def BFS(root):
    visited = [-1] * (V+1) # 가중치 저장시 -1로 초기화
    queue = deque([root])
    visited[root] = 0
    dist = [0, 0] # distance, edge

    while queue:
        n = queue.popleft()
        for e, w in graph[n]:
            if visited[e] == -1:
                visited[e] = visited[n] + w
                queue.append(e)
                if dist[0] < visited[e]:
                    dist = visited[e], e
    return dist

dist, node = BFS(1) # 임의 노드에서 최대 거리
dist, node = BFS(node) # 해당 노드에서 또 최대 거리
print(dist)
