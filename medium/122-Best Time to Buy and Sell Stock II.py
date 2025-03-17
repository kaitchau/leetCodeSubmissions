class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        res=0
        for i in range(1,len(prices)):
            sell=prices[i]
            if buy>sell:
                buy=sell
            elif sell>=buy:
                res+=sell-buy
                buy=sell
        return res
