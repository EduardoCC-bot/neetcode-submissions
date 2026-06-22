class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ("+", "-", "*", "/")
        
        for s in tokens:
            if s in op:
                if s == "+":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a + b)
                if s == "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)

                if s == "*":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a * b)
                if s == "/":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int (b / a))
            else:
                stack.append(int(s))

        return stack[-1]
        