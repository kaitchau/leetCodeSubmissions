import re 
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        set_t = set(t)
        for letter in set_t:
            t_ct = len(re.findall(letter,t))
            s_ct = len(re.findall(letter,s))
            if t_ct != s_ct:
                return False
        if set_t != set(s):
            return False        
        return True

#

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shash={}
        thash={}
        for c in s:
            if c in shash:
                shash[c]+=1
            else:
                shash[c]=1
        for c in t:
            if c in thash:
                thash[c]+=1
            else:
                thash[c]=1
        return shash==thash
        