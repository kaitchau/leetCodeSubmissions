class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ct = 0
        for x in range(len(nums)):
            for y in range(len(nums)):
                if nums[x]==nums[y] and x < y:
                    ct+=1

        return ct
        