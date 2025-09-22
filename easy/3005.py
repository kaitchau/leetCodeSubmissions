class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        print(c)
        res=0
        freq = 0
        for key,val in  c.items():
            if val == freq:
                res+=1
            elif val>freq:
                freq = val
                res=1
        return res*freq
                 
