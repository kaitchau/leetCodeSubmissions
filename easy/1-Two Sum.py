#O(N^2) time complexity
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_len = len(nums)
        for x in range(nums_len):
            for y in range(nums_len):
                if(y>x and nums[x]+nums[y]==target):
                    return [x,y]

#

#O(N) time complexity?
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_len = len(nums)
        for i in range(nums_len):
            try:
                j = nums[i+1:nums_len+1].index(target-nums[i])
                return [i,j+i+1]
            except:
                continue

#

#O(N) time complexity
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in prev:
                return [i,prev[diff]]
            prev[n]=i