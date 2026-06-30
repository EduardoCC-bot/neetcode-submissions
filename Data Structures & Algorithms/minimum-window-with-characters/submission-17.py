class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        best_l  = 0
        res = float('inf')
        t_count = defaultdict(int)
        window = defaultdict(int)
        match_count = len(t)

        for i in range(len(t)):
            t_count[t[i]]+=1

        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in t_count and window[s[r]] <= t_count[s[r]]:
                match_count -= 1
        
            while match_count == 0:
                if (r - l + 1) < res:
                    res = r - l + 1
                    best_l  = l
                window[s[l]] -= 1
                if window[s[l]] < t_count[s[l]]:
                    match_count+=1
                l+=1
        return "" if res == float('inf') else s[best_l : best_l + res]


