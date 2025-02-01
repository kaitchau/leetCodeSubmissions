class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        if nums[left]>=target:
            return left
        if nums[right]<=target:
            if nums[right]==target:
                return right
            return right+1
        while right-left>0:
            middle = (right+left)//2
            print(middle)
            if nums[middle]<=target and nums[middle+1]>target:
                print(str(nums[middle])+"<="+str(target)+"<"+str(nums[middle+1]))
                if nums[middle]<target:
                    return middle+1
                return middle
            elif nums[middle]>=target:
                right = middle
            elif nums[middle]<target:
                left=middle
