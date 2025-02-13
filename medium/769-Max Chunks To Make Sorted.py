class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        k=arr[0]
        res=0
        for i,x in enumerate(arr):
            k=max(k,x)
            if k==i:
                res+=1
        return res
