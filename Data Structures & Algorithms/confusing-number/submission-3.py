class Solution:
    def confusingNumber(self, n: int) -> bool:
        reversed = {0:0,1:1,8:8,6:9,9:6}
        number = 0
        originalnum = n
        while n:
            digit = n % 10
            if digit not in reversed:
                return False
            number = number*10 + reversed[digit]
            n //= 10
        return number != originalnum