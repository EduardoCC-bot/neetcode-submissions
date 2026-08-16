class Solution:
    def isHappy(self, n: int) -> bool:
        """
        curr = n
        101
        mod 101 = 1
        curr += module ^ 2
        """
        curr = 0
        seen = set()
        while n not in seen:
            seen.add(n)
            n = self.sumOfSquares(n)
            if n == 1: return True
        
        return False

    def sumOfSquares(self, n: int)-> int:
        output = 0
        while n:
            digit = n % 10
            digit = digit**2
            output += digit
            n = n // 10
        return output



