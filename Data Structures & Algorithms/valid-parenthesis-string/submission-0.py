class Solution:
    def checkValidString(self, s: str) -> bool:
        leftStack = []
        starStack = []

        for i, c in enumerate(s):
            if c == '(': leftStack.append(i)
            elif c == '*': starStack.append(i)
            else:
                if not leftStack and not starStack:
                    return False
                
                if leftStack:
                    leftStack.pop()
                else:
                    starStack.pop()
                
        
        while leftStack and starStack:
            if leftStack.pop() > starStack.pop():
                return False
        
        return not leftStack