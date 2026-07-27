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

        l1 = l2 = 0
        s = []
        while l1 < len(word1) and l2 < len(word2):
            s.append(word1[l1])
            s.append(word2[l2])
            l1 += 1
            l2 += 1
        if l1 < len(word1): 
            s += word1[l1:]
        if l2 < len(word2):
            s += word2[l2:]
        return "".join(s)
