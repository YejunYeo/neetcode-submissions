class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        for r in range (9):
            for c in range (9):
                boxcord = (r//3, c//3)
                if (board[r][c] == "."):
                    continue
                elif (board[r][c] in cols[c]):
                    return False
                elif (board[r][c] in rows[r]):
                    return False
                

                elif (board[r][c] in boxes[boxcord]):
                    return False
                
                else:
                    cols[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    boxes[boxcord].add(board[r][c])
        
        return True

                
        
        
                