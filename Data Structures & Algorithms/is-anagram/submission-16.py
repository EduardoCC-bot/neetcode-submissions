class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        for l in s:
            print(s.count(l))
            print(t.count(l))
            if(s.count(l) != t.count(l)):
                return False
        return True
        
         
        