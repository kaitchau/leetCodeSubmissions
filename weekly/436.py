#Q1
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        black=[[] for _ in range(n)]
        blue=[[] for _ in range(n-1)]
        for r in range(n):
            for c in range(n):
                if r>=c:
                    print(1)
                    black[r-c].append(grid[r][c])
                else:
                    blue[c-r-1].append(grid[r][c])
        for arr in black:
            arr.sort(reverse=True)
        for arr in blue:
            arr.sort()
        for r in range(n):
            for c in range(n):
                if r>=c:
                    grid[r][c]=black[r-c][c]
                else:
                    grid[r][c]=blue[c-r-1][r]
        #print(black)
        #print(blue)
        return grid

#

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        for r in range(n):
            if r == 0:
                arr=[]
                for c in range(n):
                  arr.append(grid[c][c])
                arr.sort(reverse=True)
                for c in range(n):
                    grid[c][c]=arr[c]
            else:
                inc = []
                dec = []
                for c in range(n-r):
                    inc.append(grid[c][c+r])
                    dec.append(grid[c+r][c])
                inc.sort()
                dec.sort(reverse=True)
                for c in range(n-r):
                    grid[c][c+r]=inc[c]
                    grid[c+r][c]=dec[c]
        return grid
                    