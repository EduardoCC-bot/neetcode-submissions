class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        stack = []
        seen = set()
        numIslands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1' and (i, j) not in seen:
                    numIslands += 1
                    stack.append((i,j))
                    seen.add((i,j))
                while stack:
                    si, sj = stack.pop()   
                    if si + 1 < ROWS and grid[si+1][sj] == '1' and (si+1,sj) not in seen:
                        stack.append((si+1, sj))
                        seen.add((si+1, sj))
                    if sj + 1 < COLS and grid[si][sj+1] == '1' and (si, sj+1) not in seen:
                        stack.append((si, sj+1))
                        seen.add((si, sj+1))
                    if si-1 >= 0 and grid[si-1][sj] == '1' and (si-1, sj) not in seen:
                        stack.append((si-1, sj))
                        seen.add((si-1, sj))
                    if sj - 1 >= 0 and grid[si][sj-1] == '1' and (si, sj-1) not in seen:
                        stack.append((si, sj-1))
                        seen.add((si, sj-1))
        return numIslands

