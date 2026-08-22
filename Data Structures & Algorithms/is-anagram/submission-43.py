class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        chars_on_s = defaultdict(int)
        chars_on_t = defaultdict(int)

        for i in range(len(s)):
            chars_on_s[s[i]] += 1
            chars_on_t[t[i]] += 1
        

        return chars_on_s == chars_on_t

