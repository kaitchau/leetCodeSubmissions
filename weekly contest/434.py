class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        ct=0
        for i in range(len(nums)-1):
            if (sum(nums[0:i+1])-sum(nums[i+1:len(nums)]))%2==0:
                ct+=1
        return ct