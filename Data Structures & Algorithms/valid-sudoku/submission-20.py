class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        First thing that comes to my mind is to use a sets
        for each validacition that we have to do, a set with the 
        numbers that we have in the columns as the same in rows and diag
        """

        rows_seen = defaultdict(set)
        cols_seen = defaultdict(set)
        diag_seen = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".": continue
                if (board[i][j] in rows_seen[i] 
                    or board[i][j] in cols_seen[j] 
                    or board[i][j] in diag_seen[(i // 3, j//3)]):
                    return False
                rows_seen[i].add(board[i][j])
                cols_seen[j].add(board[i][j])
                diag_seen[(i//3, j//3)].add(board[i][j])
                
        return True



