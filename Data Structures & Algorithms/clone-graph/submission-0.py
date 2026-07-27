"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        res = []
        hashMap = {}

        def dfs(node):
            if node in hashMap:
                return hashMap[node]
            copy = Node(node.val)
            hashMap[node] = copy
            
            for nighbor in node.neighbors:
                copy.neighbors.append(dfs(nighbor))
            return copy

        return dfs(node) if node else None


