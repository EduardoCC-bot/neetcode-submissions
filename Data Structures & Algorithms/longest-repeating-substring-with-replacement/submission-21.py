class Solution:
    def characterReplacement(self, s: str, k: int) -> int:    
        hasMap = defaultdict(int)
        l = 0
        res = 0
        maxfrec = 1
        for r in range(0,len(s)):
            hasMap[s[r]] += 1
            maxfrec = max(maxfrec, hasMap[s[r]])
            w = r - l + 1
            if w - maxfrec > k:
                hasMap[s[l]] -= 1
                l += 1
            else:
                res = max(res, w)
        return res