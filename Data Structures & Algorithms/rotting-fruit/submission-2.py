class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque([])
        vectors = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()
        best = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                    visited.add((i,j))
                
        while queue:
            row, col, time = queue.popleft()

            for dx, dy in vectors:
                nr, nc = row + dx, col + dy

                if (nr in range(rows) and
                nc in range(cols) and
                (nr, nc) not in visited and
                grid[nr][nc] == 1
                ):
                    grid[nr][nc] = 2
                    visited.add((nr,nc))
                    queue.append((nr,nc, time + 1))
            best = max(best, time)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return best

