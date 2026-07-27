class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        word1 = "abc", word2 = "xyz"
        l1 = a 
        l2 = x
        s += ax
        l1 = b
        l2 = 
        """
        n = len(word1)
        m = len(word2)
        m
        l1 = l2 = 0
        s = []
        while l1 < n or l2 < m:
            if l1 <n : s.append(word1[l1])
            if l2 < m: s.append(word2[l2])
            l1 += 1
            l2 += 1
        return "".join(s)
