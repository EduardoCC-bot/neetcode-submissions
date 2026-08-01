class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        s  =  "/neetcode/practice//...///../courses"
        stk = [courses,/, .., //]
        """
        stack = []
        paths = path.split("/")

        for curr in paths:
            if curr == "..":
                if stack:
                    stack.pop()
            elif curr != "" and curr != ".":
                stack.append(curr)
            
        return "/" + "/".join(stack)
            
