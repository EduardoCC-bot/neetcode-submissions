class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = set(["+", "-", "*", "/"])
        for s in tokens:
            if s in op:
                a = stack.pop()
                b = stack.pop()
                if s == "+":
                    stack.append(a + b)
                elif s == "-":
                    stack.append(b - a)
                elif s == "*":
                    stack.append(a * b)
                elif s == "/":
                    stack.append(int(b / a))
            else:
                stack.append(int(s))

        return stack[-1]
        