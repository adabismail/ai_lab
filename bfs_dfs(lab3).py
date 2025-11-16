from collections import defaultdict, deque

# Build graph
adj = defaultdict(list)
adj[1] = [2, 3]
adj[2] = [4, 5]
adj[3] = [6]

# DFS (recursive)
def dfs(node, visited):
    visited.add(node)
    print(node, end=" ")
    for child in adj[node]:
        if child not in visited:
            dfs(child, visited)

# BFS (queue)
def bfs(start):
    visited = set()
    q = deque([start])
    visited.add(start)

    while q:
        node = q.popleft()
        print(node, end=" ")
        for child in adj[node]:
            if child not in visited:
                visited.add(child)
                q.append(child)

# Run
print("DFS:", end=" ")
dfs(1, set())

print("\nBFS:", end=" ")
bfs(1)
