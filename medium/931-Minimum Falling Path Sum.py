class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N=len(matrix)
        for r in range(N):
            for c in range(N):
                if r!=0:
                    left = inf if c<1 else matrix[r-1][c-1]
                    middle = matrix[r-1][c]
                    right = inf if c>=N-1 else matrix[r-1][c+1]
                    matrix[r][c] = matrix[r][c] + min(left,middle,right)
        return min(matrix[-1])