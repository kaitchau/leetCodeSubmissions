#O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ''
        for c in s:
            if c.isalpha():
                palindrome+= c.lower()
            elif c.isdigit():
                palindrome+=c
        return palindrome == palindrome[::-1]

#

#O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ''
        for c in s:
            if c.isalnum():
                palindrome+=c.lower()
        return palindrome == palindrome[::-1]
