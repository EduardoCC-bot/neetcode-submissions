class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0 
        l,  r = 0, 1 
        window = set(s[l])
        res = 1
        while l < r and r < len(s):
            if s[r] in window:
                while s[r] in window:
                    window.remove(s[l])
                    l+=1
            res = max(res, r - l + 1)
            window.add(s[r])
            r+=1
        return res
