class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        ct=0
        subbox=[[],[],[]]
        for i in range(n):
            row = board[i]
            row_digi = ''.join(c for c in row if c.isdigit())
            if len(row_digi) != len(set(row_digi)):
                return False

            col = []
            for j in range(n):
                col.append(board[j][i])
                if j<3:
                    subbox[0].append(board[i][j])
                elif 3<=j<6:
                    subbox[1].append(board[i][j])
                else:
                    subbox[2].append(board[i][j])
            col_digi = ''.join(c for c in col if c.isdigit())
            if len(col_digi) != len(set(col_digi)):
                return False
            
            ct+=1
            if ct==3:
                for k in range(3):
                    box=subbox[k]
                    boxes = ''.join(c for c in box if c.isdigit())
                    if len(boxes) != len(set(boxes)):
                        return False
                ct=0
                subbox=[[],[],[]]
        return True
            