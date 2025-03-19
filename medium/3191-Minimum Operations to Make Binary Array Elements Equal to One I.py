class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        for i in range(n-2):
            if nums[i]==0:
                res+=1
                nums[i]= not nums[i]
                nums[i+1]= not nums[i+1]
                nums[i+2]= not nums[i+2]
        return res if len(set(nums))=1 else -1

