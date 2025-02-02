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

#

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        numfreq={}
        for n in nums:
            if n in numfreq:
                numfreq[n]+=1
            else:
                numfreq[n]=1
        freqnum = defaultdict(list)
        for num, freq in numfreq.items():
            freqnum[freq].append(num)        
        sorted_dict = dict(sorted(freqnum.items()))
        for key in sorted_dict:
            for item in sorted_dict[key]:
                ans.append(item)
        return ans[-k:]
        
#

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for n in nums:
            if n in freqs:
                freqs[n]+=1
            else:
                freqs[n]=1
        max_freq = max(freqs.values())
        buckets = [[] for _ in range(max_freq+1)]
        for n in freqs:
            buckets[freqs[n]].append(n)
        print(buckets)
        ans=[]
        for i in range(max_freq,0,-1):
            for item in buckets[i]:
                ans.append(item)
                if len(ans)==k:
                    return ans