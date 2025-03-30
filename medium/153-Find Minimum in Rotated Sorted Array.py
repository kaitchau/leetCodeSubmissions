class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        ll,rr=l,r
        if nums[l]<nums[r]:
            return nums[l]
        while l<=r:
            m=l+(r-l)//2
            v=nums[m]
            if m!=rr and v>nums[m+1]:
                return nums[m+1]
            elif m!=ll and nums[m-1]>v:
                return v
            elif nums[ll]<v:
                l=m+1
            else:
                r=m-1
        return nums[l]