#O(n) solution
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c_cts = Counter(text)
        max_ct=0
        while True:
            if c_cts['b']<(max_ct+1):
                break
            if c_cts['a']<(max_ct+1):
                break
            if c_cts['l']<(max_ct+1)*2:
                break
            if c_cts['o']<(max_ct+1)*2:
                break
            if c_cts['n']<(max_ct+1):
                break
            max_ct+=1
        return max_ct

#

#O(n) solution
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cts = Counter(text)
        max_ct=min(cts['b'],cts['a'],cts['l']//2,cts['o']//2,cts['n'])
        return max_ct
