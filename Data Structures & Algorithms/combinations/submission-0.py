class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []

        def helper(i, curr, combinations, n, k):
            if len(curr) == k:
                combinations.append(curr.copy())
                return
            if i > n:
                return
            #Desision of append the number
            curr.append(i)
            helper(i+1, curr, combinations, n, k)
            curr.pop()
            #desision of not append the number
            helper(i+1, curr, combinations, n, k)


        helper(1, [], combinations, n, k)
        return combinations
