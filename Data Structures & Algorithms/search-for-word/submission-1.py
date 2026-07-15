class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        seen = set()
        i = 0
        def dfs(i, row, col):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or (row,col) in seen or word[i] != board[row][col]:
                return False
            
            seen.add((row, col))
            if i == len(word)-1:
                return True
            else:
                if dfs(i+1, row + 1, col):return True
                if dfs(i+1, row - 1, col):return True
                if dfs(i+1, row, col + 1):return True
                if dfs(i+1, row, col - 1):return True
                seen.remove((row, col))
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c):
                    return True
        return False

        
        
            
                
