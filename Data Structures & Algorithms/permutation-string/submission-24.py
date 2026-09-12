class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        window = [0] * 26
        mapa = [0] * 26
        l = 0
        n = len(s1)
        
        for i in range(n):
            window[ord(s2[i]) - ord('a')]+=1
            mapa[ord(s1[i]) - ord('a')]+=1
        if window == mapa:
            return True

        for r in range(n, len(s2)):
            window[ord(s2[r]) - ord('a')] += 1
            window[ord(s2[l]) - ord('a')] -= 1
            l+=1
            if window == mapa:
                return True
        
        return False
            