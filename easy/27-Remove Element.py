class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)

#

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index=0
        for n in nums:
            if n!=val:
                nums[index]=n
                index+=1
        return index