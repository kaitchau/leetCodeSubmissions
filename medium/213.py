class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        memo=[-1]*n
        def dfs(i):
            if i>n-2:
                return 0
            if memo[i]!=-1:
                return memo[i]
            memo[i]=max(dfs(i+1), nums[i]+dfs(i+2))
            return memo[i]
        memo2=[-1]*n
        def dfs2(j):
            if j>n-1:
                return 0
            if memo2[j]!=-1:
                return memo2[j]
            memo2[j]=max(dfs2(j+1), nums[j]+dfs2(j+2))
            return memo2[j]
        return max(dfs(0),dfs2(1))