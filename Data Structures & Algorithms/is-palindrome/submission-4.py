class Solution:
    def isPalindrome(self, s: str) -> bool:
        copy = ""

        for c in s:
            if(c.isalnum()):
                copy += c.lower()
        return copy == copy[::-1]
