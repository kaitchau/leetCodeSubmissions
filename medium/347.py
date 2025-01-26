class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        freq=defaultdict(list)
        ans=[]
        ct=1
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                ct+=1
            else:
                freq[ct].append(nums[i-1])
                ct=1
        freq[ct].append(nums[len(nums)-1])
        sorted_freq = dict(sorted(freq.items()))
        for key in sorted_freq:
            ans.extend(sorted_freq[key])
        return ans[-k:]