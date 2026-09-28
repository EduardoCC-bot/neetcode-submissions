class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = defaultdict(int)
        l = 0
        res = 0
        maxfrec = 1
        for r in range(0, len(s)):
            freqMap[s[r]] += 1
            maxfrec = max(freqMap[s[r]], maxfrec)

            while (r - l + 1) - maxfrec > k:
                freqMap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
    
        return res