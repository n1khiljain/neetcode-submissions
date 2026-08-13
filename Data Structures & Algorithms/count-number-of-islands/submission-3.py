class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0
        vectors = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(r,c):
            queue = collections.deque([(r,c)])
            
            while queue:
                row, col = queue.popleft()
                
                for dx, dy in vectors:
                    nr, nc = row + dx, col + dy

                    if (nr in range(rows) and 
                    nc in range(cols) and
                    (nr, nc) not in visited and
                    grid[nr][nc] == "1"
                    ):
                        queue.append((nr,nc))
                        visited.add((nr,nc))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and ((i,j) not in visited):
                    bfs(i, j)
                    count += 1
        return count

