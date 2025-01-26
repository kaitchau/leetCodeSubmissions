class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones)>1:
            if stones[-1]==stones[-2]:
                stones.pop()
                stones.pop()
            else:
                stones[-1]=stones[-1]-stones[-2]
                stones.pop(-2)
                stones.sort()
        if len(stones)==0:
            return 0
        return stones[0]