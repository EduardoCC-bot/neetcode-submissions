class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0: return True
        if len(edges) != n - 1: return False

        adjList = {}
        for src, dst in edges:
            if src not in adjList:
                adjList[src] = []
            if dst not in adjList:
                adjList[dst] = []
            adjList[src].append(dst)
            adjList[dst].append(src)

        
        visit = set()
        def dfs(node, parent):
            if node in visit:
                return False
            visit.add(node)
            for n in adjList[node]:
                if n != parent and not dfs(n, node):
                    return False
            return True        
        return dfs(0, -1) and len(visit) == n
        
        




