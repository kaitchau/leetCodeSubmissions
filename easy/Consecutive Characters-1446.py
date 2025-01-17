class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        substrs = []
        buffer = ""
        last_c = s[0]
        for i in range(len(s)):
            if s[i]!=last_c or i==len(s)-1:
                if s[i]==last_c and i==len(s)-1:
                    buffer+=s[i]
                substrs.append(buffer)
                buffer = s[i]
                last_c=s[i]
                continue
            buffer+=s[i]
        max_len = 1
        print(str(substrs))
        for item in substrs:
            if len(item) > max_len:
                max_len = len(item)
        return max_len