class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            start = max(0,i-nums[i])
            summ = sum(nums[start:i])
            total+=summ
        return total

import itertools
class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        total=0
        for L in range(k,0,-1):
            combos = itertools.combinations(nums,L)
            for combo in combos:
                summ = max(combo)+min(combo)
                total+=summ
        return total % (10**9 + 7)
