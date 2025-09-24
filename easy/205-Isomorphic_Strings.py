class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        m1 = {} #map s to t
        m2 = {} #map t to s
        if n!=len(t):
            return False
        for i,c in enumerate(s):
            if c not in m1 and t[i] not in m2:
                m1[c]=t[i]
                m2[t[i]]=c
            if c in m1:
                if m1[c]!=t[i]:
                    return False
            if t[i] in m2:
                if m2[t[i]]!=c:
                    return False
        return True