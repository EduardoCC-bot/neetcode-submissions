class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        seen = set()
        ROWS, COLS = len(image), len(image[0])
        oldColor = image[sr][sc]
        if oldColor == color: return image

        def dfs(r,c):
            if (min(r,c) < 0 or r >= ROWS or c >= COLS 
                or image[r][c] != oldColor or (r,c) in seen ):
                return
            #Change color to new one
            image[r][c] = color
            seen.add((r,c))
            dfs(r + 1,c)
            dfs(r - 1,c)
            dfs(r,c + 1)
            dfs(r,c - 1)
            
        dfs(sr, sc)
        
        return image


