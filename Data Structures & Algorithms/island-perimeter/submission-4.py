class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        per = 0
        neighbors = ((1,0), (-1,0), (0,1), (0,-1))
        q  = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    q.append((r,c))
                    visited.add((r,c))
        
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr, dc in neighbors:
                    nr = r + dr
                    nc = c + dc
                    if (min(nr,nc) < 0 or nr >= ROWS or nc >= COLS 
                        or grid[nr][nc] == 0):
                        per += 1
        return per



        