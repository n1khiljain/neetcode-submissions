class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0,0
        vector = [(0,1), (0,-1), (1,0), (-1,0)]

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1 #counting fresh oranges
                if grid[r][c] == 2:
                    q.append((r,c)) # adding rotting oranges to queue
            
        # bfs
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in vector:
                    nr, nc = r + dr, c + dc
                    # if in bounds and fresh
                    if (nr in range(rows) and
                        nc in range(cols) and
                        grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
                    
        
                


                
