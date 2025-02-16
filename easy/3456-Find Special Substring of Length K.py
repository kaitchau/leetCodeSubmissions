class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        prev=''
        curr=s[0]
        ct=0
        for i,c in enumerate(s):
            if c==curr:
                ct+=1
            else:
                prev=s[i-1]
                curr=c
                ct=1
            if ct==k:
                if prev!=c and (i==len(s)-1 or c!=s[i+1]):
                    return True
        return False