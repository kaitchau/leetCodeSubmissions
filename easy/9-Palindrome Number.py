class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string_x = str(x)
        reverse = string_x[::-1]
        if string_x==reverse:
            return True
        else:
            return False