class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        res -> []
        asteroids = [2,4,-4,-1]
        ast.pop -> -1
        
        is a greater element on res
        no 
        is a smallest element on res
        no
        append -1

        ast.pop -> -4
        is diferent sign the top of stack
        no
        res.append -4
        res = [-1,-4]

        ast.pop -> 4
        is diferent sign the top of stack
        if 4 == res[-1]
            res.pop
            continue
        if 4 > res[-1]
            res.pop
        res.append(4)
        """

        stack = []

        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
        return stack







