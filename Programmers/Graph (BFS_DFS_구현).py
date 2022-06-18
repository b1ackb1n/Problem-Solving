# 유향그래프
# 노드의 element는 set()으로 묶기
graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1

from collections import deque
# BFS: Queue (Deque)
def BFS(graph, root):
    visited = []
    queue = deque([root])
    # 인접한 노드 중 방문하지 않은 노드만 큐에 넣음

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited

# DFS: Stack
def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            stack.append(n)
            stack += graph[n] - set(visited)
    return visited
