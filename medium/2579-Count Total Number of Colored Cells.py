# O(n) solution
class Solution:
    def coloredCells(self, n: int) -> int:
        res=1
        for i in range(n):
            res+=(i)*4 # calculates the perimeter each time
        return res

#O(1) solution
class Solution:
    def coloredCells(self, n: int) -> int:
        return n**2+(n-1)**2