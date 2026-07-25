class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r, c = row1, col1
        res = 0
        while r <= row2:
            while c <= col2:
                res+=self.matrix[r][c]
                c+=1
            c = col1
            r+=1

        return res
        """
        We know that row1 is where to start on the matrix and also col1
        """


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)