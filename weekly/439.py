#Q1 
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        seqs=[]
        res=-1
        for i in range(n-k+1):
            seqs.append(nums[i:i+k])
        nums.sort()
        for n in range(n-1,-1,-1):
            ct=0
            for seq in seqs:
                if nums[n] in seq:
                    print('hi')
                    ct+=1
            if ct==1:
                res=max(res,nums[n])
        return res