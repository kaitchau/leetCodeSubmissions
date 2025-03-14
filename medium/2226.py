# O(nlog(total//k)) solution binary search
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)
        if total<k:
            return 0
        left=1
        right=total//k
        res=0
        while left<=right:
            mid=(left+right)//2
            ct=0
            for candy in candies:
                ct+=candy//mid
            if ct>=k:
                left=mid+1
                res=max(res,mid)
            elif ct<k:
                right=mid-1
        return res