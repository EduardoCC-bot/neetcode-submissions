class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Again the firts thing that comes to my mind is to use a DFS
        to look for every posible possition on the matrix when we found 
        a 1 (land), so the main idea that I have of the algorith is to
        look from the beginin of the matrix lets say [0,0], look if is 1 o 0
        if it's 0 mark it as seen an continue if it's 1 start the dfs 
        also we are goint to mark visitted all the lands that we have, and count 1
        and continue
        """
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        def dfs(r,c):
            nonlocal count
            if (min(r,c) < 0 or r >= ROWS or c >= COLS or grid[r][c] != '1'):
                return 0
            grid[r][c] = '-1'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return 1


        for r in range(ROWS):
            for c in range(COLS):
                count += dfs(r,c)
        return count