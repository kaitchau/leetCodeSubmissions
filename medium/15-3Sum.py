class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        for i in range(n):
            store={}
            for j in range(i+1,n):
                diff = 0-nums[i]-nums[j]
                print(str(nums[i])+','+str(nums[j])+','+str(diff))
                if diff in store and store[diff]!=i and store[diff]!=j:
                    print('hi')
                    k=store[diff]
                    res.append([nums[i],nums[j],nums[k]])
                store[nums[j]]=j
        return res