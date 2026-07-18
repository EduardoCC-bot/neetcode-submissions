class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        hashSet = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(s)):
            hashSet[s[r]]+=1
            
            while len(hashSet) > 2:
                hashSet[s[l]]-=1
                if hashSet[s[l]] == 0:
                    hashSet.pop(s[l])
                l+=1
        
            res = max(res, r - l + 1) 
                    
        return res
        

            
                