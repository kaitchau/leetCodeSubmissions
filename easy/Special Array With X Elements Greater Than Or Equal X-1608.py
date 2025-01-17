class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for x in range(max(nums)+1):
            filtered_nums = filter(lambda y: y>=x, nums)
            print(str(len(filtered_nums))+","+str(x))
        
            if len(filtered_nums) == x:
                return x
        return -1