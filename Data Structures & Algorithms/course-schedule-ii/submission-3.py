class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
         res []
            [0, 1]
        Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]
        
        seenCourses = (0, 4, 3, 1)
         = (1, 0, 3, 4)

        AdjList
         0 : [1]
         2 : [1]
         3 : [1]
         4 : [3]
         1 : []

        """
        adjList = {c : [] for c in range(numCourses)}

        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        """for crs, prst in prerequisites:
            if crs not in adjList:
                adjList[crs] = []
            if prst not in adjList:
                adjList[prst] = []
            adjList[crs].append(prst)
        """
        res = []
        cycle = set()
        seen = set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in seen:
                return True
            
            cycle.add(crs)
            for pre in adjList[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            seen.add(crs)
            res.append(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return res

                    
