class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        g = [1,2,3] s = [1,1]

        """
        g.sort()
        s.sort()

        i = j = 0
        while i < len(g):
            while j < len(s) and g[i] > s[j]:
                j+=1
            if j == len(s):
                break
            i+=1
            j += 1
        return i

