class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        map -> {k: s} : 2 : "abc"

        recurisive funtion taking the desicion of add or not the next string
        digits "34"
        3 : "def" i -> 0 
        4 : "ghi" j -> 

        know n = length digits
        helper(i, j,n, curr)
        lenght of current == 2
            yes : append that to a array resutl
                return
            no
            append to curr the s[i]
        
        for loop for each i in 3 
            for each j in 4
                add c to curr
                helper function
                pop c 

        i = 0
        ["dg"]
        c = "d" -> "ghi" j= 0 moving j++
        c = "d" -> "hi"  j = 
        
        what happend if theres and empy digits?
            we need to return ""
        """
        hashmap = {2:"abc",3:"def", 4:"ghi",5:"jkl",6:"mno",7:"pqrs", 8:"tuv", 9:"wxyz" }
        res = []
        if not digits: return []
        def helper(indx, curr, i):
            if i >= len(digits):
                res.append("".join(curr.copy()))
                return
                
            for c in hashmap[int(digits[indx])]:
                curr.append(c)
                helper(indx+1, curr, i + 1)
                curr.pop()
        helper(0, [], 0)
        return res
        




