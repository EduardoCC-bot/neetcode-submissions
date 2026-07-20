class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visitSet = set()

        def dfs(curr):
            if curr in visitSet:
                return False
            if preMap[curr] == []:
                return True
            
            visitSet.add(curr)
            for pre in preMap[curr]:
                if not dfs(pre):return False
            
            visitSet.remove(curr)
            preMap[curr] = []
            return True


        for crs in range(numCourses):
            if not dfs(crs): return False
        return True