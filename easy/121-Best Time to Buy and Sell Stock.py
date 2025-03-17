#O(n) solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        n=len(prices)
        prev=prices[0]
        for i in range(1,n):
            if prev>prices[i]:
                prev=prices[i]
            res=max(res,prices[i]-prev)
        return res

