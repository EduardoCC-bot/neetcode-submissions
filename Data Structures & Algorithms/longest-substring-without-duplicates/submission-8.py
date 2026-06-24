class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        view = set()
        l = 0
        maxlen = 0
        for r in range(len(s)):
            while s[r] in view:
                view.remove(s[l])
                l+=1
            view.add(s[r])
            maxlen = max(maxlen, r-l + 1)
        return maxlen


