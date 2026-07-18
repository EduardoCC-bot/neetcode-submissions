class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        hashSet = defaultdict(int)
        cnt = 0
        l = 0
        res = 0
        for r in range(len(s)):
            if hashSet[s[r]] == 0: cnt+=1 
            hashSet[s[r]]+=1

            while cnt > k:
                hashSet[s[l]]-=1
                if hashSet[s[l]] == 0:
                    cnt-=1
                l+=1
            
            res = max(res, r-l+1) 

        return res
            