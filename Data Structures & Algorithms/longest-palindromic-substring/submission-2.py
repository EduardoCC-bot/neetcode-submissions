class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        ababd

        abbc
        """
        res = ""
        for i in range(len(s)):
            
            #Even abbc
            l, r= i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            word1 = s[l+1:r]
            if len(word1) > len(res):
                res = word1
            
            #Odd ababd
            l = r = i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            word2 = s[l+1:r]
            if len(word2) > len(res):
                res = word2
        
        return res