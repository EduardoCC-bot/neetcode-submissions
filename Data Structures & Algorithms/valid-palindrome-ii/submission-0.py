class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        prefix, sufix


        oscobasoso
        o  o
        s  s
        
        c  o

        o  s
        """
        if s == s[::-1]:return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l + 1:r + 1], s[l : r] 
                return (skipL == skipL[::-1] or skipR == skipR[::-1])
            l+=1
            r-=1
        return True     

