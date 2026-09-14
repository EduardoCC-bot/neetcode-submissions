class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        l            r
t       [1 ][2 ][3 ][4 ]
        [5 ][6 ][7 ][8 ]
        [9][10][11][12]
        [13][14][15][16]
        """
        
        n = len(matrix)
        l, r = 0, n - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                topleft = matrix[top][l + i]

                matrix[top][l + i] = matrix[bottom - i][l]

                matrix[bottom - i][l] = matrix[bottom][r - i ]

                matrix[bottom][r - i] = matrix[top + i][r]

                matrix[top + i][r] = topleft

            r -= 1
            l += 1
        
    




        