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