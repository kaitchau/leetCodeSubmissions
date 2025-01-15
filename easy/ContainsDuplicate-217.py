class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = {}
        for num in nums:
            if dict.get(num) == None:

                dict.update({num:num})
            else:
                return True
        return False
        