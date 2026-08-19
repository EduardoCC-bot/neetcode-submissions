class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = s.split().pop()
        return len(res)