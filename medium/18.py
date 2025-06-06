class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        for i,num in enumerate(nums):
            for j,num2 in enumerate(nums[i+1:]):
                store = defaultdict(int)
                for k,n in enumerate(nums[j+1:]):
                    diff = target-num-num2-n
                    if diff in store:
                        quad = [num,num2,diff,n]
                        quad.sort()
                        res.add(tuple(quad))
                    else:
                        store[n]=k
        return list(res)