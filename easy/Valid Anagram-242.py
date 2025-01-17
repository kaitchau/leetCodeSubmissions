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

        