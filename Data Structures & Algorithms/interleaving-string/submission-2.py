class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if  len(s1) + len(s2) != len(s3):
            return False
        cache = {}
        def helper(i, j, k):
            if k == len(s3):
                return (i == len(s1)) and (j == len(s2))
            if (i,j) in cache:
                return cache[(i, j)]
            res = False
            if i < len(s1) and s3[k] == s1[i]:
                res = helper(i + 1, j, k + 1)
            if j < len(s2) and s3[k] == s2[j]:
                res = helper(i, j + 1, k + 1)
            cache[(i, j)] = res
            return res
        return helper(0,0,0)
                
