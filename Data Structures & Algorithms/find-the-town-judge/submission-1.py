class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        whoTrust = {}
        howManyTrust = defaultdict(int)

        for tr, trusted in trust:
            if tr in whoTrust:
                continue
            whoTrust[tr] = trusted
            howManyTrust[trusted] += 1
        
        for tr, trusted in trust:
            if trusted not in whoTrust and howManyTrust[trusted] == n-1:
                return trusted
        
        return -1
