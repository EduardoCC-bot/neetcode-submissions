class Solution:
    def characterReplacement(self, s: str, k: int) -> int:    
        hasMap = defaultdict(int)
        l = 0
        res = 0
        maxfrec = 1
        for r in range(0,len(s)):
            hasMap[s[r]] += 1
            maxfrec = max(maxfrec, hasMap[s[r]])
            while (r - l + 1) - maxfrec > k:
                hasMap[s[l]] -= 1
                l += 1
            else:
                res = max(res, r - l + 1)
        return res