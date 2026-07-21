class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        """
        osobaboso
        Count the number of characters that we have
        o = 4
        s = 2
        a = 1
        b = 2

        aab
        a = 2
        b = 1
        """
        cnt = 0 
        count = [0] * 26
        n = len(s)
        for i in range(n):
            count[ord(s[i]) - ord('a')] +=1  
            if count[ord(s[i]) - ord('a')] % 2 == 0:
                cnt-=1
            else:
                cnt+=1
        
        return cnt <= 1

