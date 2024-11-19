# 994. Rotting Oranges
def orangesRotting(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    numFresh = 0
    queue = deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1:
                numFresh += 1
            elif grid[i][j]==2:
                queue.append((i ,j, 0))
    
    last_time = 0
    while queue:
        i, j, time = queue.popleft()
        last_time = time
        for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:  # UDLR
            if 0<=ni<m and 0<=nj<n and grid[ni][nj]==1:
                queue.append((ni, nj, time+1))
                grid[ni][nj] = 2
                numFresh -= 1

    return last_time if numFresh==0 else -1

def orangesRotting(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    numFresh, time = 0, 0
    queue = deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1:
                numFresh += 1
            elif grid[i][j]==2:
                queue.append((i ,j))
    
    while queue and numFresh>0:
        for _ in range(len(queue)):
            i, j = queue.popleft()
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:  # UDLR
                if 0<=ni<m and 0<=nj<n and grid[ni][nj]==1:
                    queue.append((ni, nj))
                    grid[ni][nj] = 2
                    numFresh -= 1
        
        time += 1

    return time if numFresh==0 else -1