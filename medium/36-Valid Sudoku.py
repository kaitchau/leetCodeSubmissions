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

#

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [""]*9
        boxes = [["","",""],["","",""],["","",""]]
        #print(boxes)
        for i in range(9):
            row = ""
            for j in range(9):
                if board[i][j].isdigit():
                    row+=board[i][j]
                    cols[j]+=board[i][j]
                    #print(str(i//3)+","+str(j//3))
                    boxes[i//3][j//3]+=board[i][j]
            if len(row) != len(set(row)):
                #print(row)
                return False
        for col in cols:
            if len(col) != len(set(col)):
                #print(col)
                return False
        #print(boxes)
        for boxes2 in boxes:
            for box in boxes2:
                if len(box) != len(set(box)):
                    #print(box)
                    return False
        return True