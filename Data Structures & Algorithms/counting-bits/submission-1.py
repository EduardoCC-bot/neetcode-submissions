class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        0 : 0000 : 0
        1 : 0001 : 1
        2 : 0010 : 1
        3 : 0011 : 2
        4 : 0100 : 3
        5 : 0101 : 2
        6 : 0110 : 2
        7 : 0111 : 3

        [0, 1, 1, 2, 1, 2, ]
         0, 1, 2, 3, 4, 5,  
        """

        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp
        



        