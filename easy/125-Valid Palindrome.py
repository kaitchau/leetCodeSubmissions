class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ''
        for c in s:
            if c.isalpha():
                palindrome+= c.lower()
            elif c.isdigit():
                palindrome+=c
        return palindrome == palindrome[::-1]
