class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        visited = set()
        maxSize = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r,c): #r,c are row, col indices
            q = collections.deque([(r,c)]) #queue
            visited.add((r,c))
            size = 1

            while q:
                row, col = q.popleft()

                vector = [(0,1), (0,-1), (1,0), (-1,0)]
                for dr, dc in vector:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == 1 and
                        (r,c) not in visited
                    ):
                        size += 1
                        q.append((r,c))
                        visited.add((r,c))
            return size

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    size = bfs(r,c) # has to set/update size
                    maxSize = max(maxSize, size)
        
        return maxSize
