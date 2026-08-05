class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):
            q = deque([(r,c)])

            while q:
                row, col = q.popleft()

                for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nr, nc = row + dr, col + dc

                    if (nr in range(ROWS) and
                        nc in range(COLS) and
                        grid[nr][nc] == "1" and
                        (nr, nc) not in visited
                    ):
                        q.append((nr,nc))
                        visited.add((nr,nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    bfs(r,c)

        return islands