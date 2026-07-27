class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        My firts thoughts on this one it's use a DFS if the cell
        it's 0 just move to the possible moves, have an set to save visit
        cells,  
        
        """
        visited = set()
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r,c) in visited or grid[r][c] == 0:
                return 0
            visited.add((r, c))
            #Validate posible positions
            return dfs(r + 1,c) + dfs(r - 1,c) +dfs(r,c + 1) +dfs(r,c - 1) + 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    maxArea = max(maxArea, area)

        return maxArea