class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        n=len(nums)
        if total%2!=0:
            return False
        target=total/2
        memo={}
        def rec(curr_sum,i):
            if (curr_sum,i) in memo:
                return memo[(curr_sum,i)]
            if curr_sum==target:
                return True
            elif curr_sum>target or i>=n:
                return  False
            value = rec(curr_sum, i+1) or rec(curr_sum+nums[i],i+1)
            memo[(curr_sum,i)]=value
            return value
        return rec(0,0)