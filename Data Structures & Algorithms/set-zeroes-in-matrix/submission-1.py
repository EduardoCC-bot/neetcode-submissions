class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        1:1
        MATRIX[1] = [1][0][1][1]
        MATRIX[i][1]

        [1][1][1][1]
        [1][0][1][1]
        [1][1][0][1]
        [1][1][1][1]

        """
        ROWS, COLS = len(matrix), len(matrix[0])
        rows_to_zero = set()
        cols_to_zero = set()
        
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)

        for r in rows_to_zero:
            matrix[r] = [0] * COLS

        for c in cols_to_zero:
            for r in range(ROWS):
                matrix[r][c] = 0
