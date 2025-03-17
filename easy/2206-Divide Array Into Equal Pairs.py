class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        store = defaultdict(int)
        for n in nums:
            store[n]+=1
        for value in store.values():
            if value%2!=0:
                return False
        return True

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freqs=Counter(nums)
        for v in freqs.values():
            if v%2!=0:
                return False
        return True