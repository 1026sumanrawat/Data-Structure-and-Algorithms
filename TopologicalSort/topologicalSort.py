# https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = { i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visitedSet, cycle = set(), set()
        res = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visitedSet:
                return True
            cycle.add(crs)
            preq = preMap[crs] 
            for p in preq:
                if dfs(p) == False:
                    return False
            cycle.remove(crs)
            visitedSet.add(crs)
            res.append(crs)
            return True


        for num in range(numCourses):
            if dfs(num) == False:
                return []
        return res
