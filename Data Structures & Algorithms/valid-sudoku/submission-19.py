class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colsSet = defaultdict(set)
        rowsSet = defaultdict(set)
        squareSet = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in colsSet[j]
                    or board[i][j] in rowsSet[i]
                    or board[i][j] in squareSet[(i // 3, j // 3)]):
                    return False
                
                rowsSet[i].add(board[i][j])
                colsSet[j].add(board[i][j])
                squareSet[(i // 3, j // 3)].add(board[i][j])

        
        return True
