class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        IV
        
        XIV

        XLIX
        len = 4 
        '''
        mapa = {'I': 1, 'V' : 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M': 1000}
        res = 0
        for i in range(len(s)): # 0 | 1 | 2
            val = mapa[s[i]] # X:10 | L:50 | I:1
            if i+1 <= len(s) - 1 and val < mapa[s[i+1]]: 
                # 0+1:1 and 10 < 50 | 1+1:2 and 50 < 1 | 2+1:3  
                res -= val # -10
            else:
                res += val # -10 + 50 = 40
        return res

