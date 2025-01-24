class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset= set(nums)
        maxseq = 0
        for n in numset:
            if n-1 not in numset:
                ct=1
                while n+ct in numset:
                    ct+=1
                maxseq=max(maxseq,ct)
        return maxseq
