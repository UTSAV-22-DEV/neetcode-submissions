class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=[ch.lower() for ch in s if ch.isalnum()]
        s2=s1[::-1]
        return s1==s2
        