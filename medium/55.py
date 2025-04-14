class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[0]*n
        dp[0]=1
        for i,n in enumerate(nums):
            if dp[i]!=0:
                j=nums[i]
                dp[i:i+j+1]=[1]*(j+1)
        return bool(dp[-1])