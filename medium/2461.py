class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nset=set(nums[0:k+1])
        csum=sum(nums[0:k+1])
        msum=csum if len(nset)==k else 0
        for i in range(1,n-k+1):
            l,r=nums[i-1],nums[i+k-1]
            print(l)
            print(r)
            csum-=l
            csum+=r
            nset.remove(l)
            nset.add(r)
            if len(nset)==k:
                msum=max(msum,csum)
        return msum