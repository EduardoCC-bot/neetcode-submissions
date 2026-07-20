class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Recursive function
        take two desicions
            1 open another parentesis
            2 close the parentesis

        How do we know when to do 1 or 2
            if I think about it we have to close a parentesis when we have few parentesis
                    """
        res = []
        def helper(o, c,curr):
            if len(curr) == 2*n:
                res.append(curr)
                return
            
            if c < o:
                helper(o, c+1,curr + ")")
            if o < n:
                helper(o+1, c, curr + "(")
            
            

        helper(0, 0, "")
        return res

