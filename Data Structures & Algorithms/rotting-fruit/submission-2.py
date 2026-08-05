class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        minutes = -1
        q = deque()
        visited = set()
        neighbors = ((0,1), (0,-1), (1,0), (-1,0))
        freshCnt = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    freshCnt+=1
        if freshCnt == 0: return 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in neighbors:
                    nr, nc = r+dr, c+dc
                    if (min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in
                        visited or grid[nr][nc] == 0):
                        continue
                    if grid[nr][nc] == 1: freshCnt -= 1 
                    q.append((nr, nc))
                    visited.add((nr, nc))
            minutes += 1
        
        if freshCnt > 0: return -1
        return minutes


