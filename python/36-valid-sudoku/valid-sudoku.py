class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            numb_row = set()
            numb_col = set()
            numb_grid = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in numb_row:
                        return False
                    else:
                        numb_row.add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in numb_col:
                        return False
                    else:
                        numb_col.add(board[j][i])
                if board[3 * int(i/3) + int(j/3)][3 * (i % 3) + j % 3] != '.':
                    if board[3 * int(i/3) + int(j/3)][3 * (i % 3) + j % 3] in numb_grid:
                        return False
                    else:
                        numb_grid.add(board[3 * int(i/3) + int(j/3)][3 * (i % 3) + j % 3])
        return True
        