#Q1 easy O(n)
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        def op(s:str):
            res=''
            n=len(s)
            for i in range(n-1):
                a=int(s[i])
                b=int(s[i+1])
                res+=str((a+b)%10)
            return res
        while len(s)>2:
            s=op(s)
        return s[0]==s[1]

#Q2 medium O(n)
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        arr=[]
        for i,row in enumerate(grid):
            row.sort()
            newrow=[]
            for j in range(limits[i]):
                newrow.append(row.pop())
            arr+=newrow
        arr.sort()
        res=0
        while arr and k>0:
            res+=arr.pop()
            k-=1
        return res
            