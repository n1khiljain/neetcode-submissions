class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()
        visited = set()

        # push all treasure chests into queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        vector = [(0,1), (0,-1), (1,0), (-1,0)]

        # bfs
        while q:
            r, c = q.popleft()

            for dr, dc in vector:
                nr, nc = r + dr, c + dc
                if (
                    nr in range(rows) and
                    nc in range(cols) and 
                    grid[nr][nc] == INF
                ):
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr,nc))

        

        
