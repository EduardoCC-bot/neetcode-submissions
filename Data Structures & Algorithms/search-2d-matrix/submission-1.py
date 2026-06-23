class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            if target <= row[-1]:
                for i in row:
                    if i == target:
                        return True
                return False    
        return False