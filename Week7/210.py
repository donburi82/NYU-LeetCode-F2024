# 210. Course Schedule II
# Using DFS+backtracking
def topologicalSort(self, node, adj, visited, stack, path):
    visited[node] = 1
    path[node] = 1
    for i in adj[node]:
        if not visited[i]:
            if not self.topologicalSort(i, adj, visited, stack, path):
                return False
        elif path[i]:
            return False
    
    path[node] = 0
    stack.append(node)
    return True

def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    adj = [[] for _ in range(numCourses)]
    for a, b in prerequisites:
        adj[b].append(a)

    stack = []
    visited = [0]*numCourses
    path = [0]*numCourses
    for i in range(numCourses):
        if not visited[i]:
            if not self.topologicalSort(i, adj, visited, stack, path):
                return []

    return stack[::-1]

# Kahn's algorithm (BFS) - must start from nodes with in-degree of 0
def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    adj = [[] for _ in range(numCourses)]
    in_degree = [0]*numCourses
    for a, b in prerequisites:
        adj[b].append(a)
        in_degree[a] += 1

    queue = deque()
    for i in range(numCourses):
        if not in_degree[i]:
            queue.append(i)
    
    res = []
    while queue:
        node = queue.popleft()
        res.append(node)
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor]==0:
                queue.append(neighbor)

    return res if len(res)==numCourses else []