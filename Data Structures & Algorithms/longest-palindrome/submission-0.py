class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashMap = defaultdict(int)
        res = 0
        for c in s:
            hashMap[c] += 1 
            if hashMap[c] % 2 == 0:
                res += 2
        
        for c in hashMap.values():
            if c % 2:
                res+=1
                break

        return res
        
