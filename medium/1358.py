class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq={'a':0,'b':0,'c':0}
        n=len(s)
        l,res=0,0
        for r in range(n):
            freq[s[r]]+=1
            while freq['a']>0 and freq['b']>0 and freq['c']>0:
                freq[s[l]]-=1
                l+=1
                res+=n-r
        return res