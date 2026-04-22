class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #[0 -> 1] [0 -> 2], [1 -> 3] [3 -> 4], [5 -> 4] [1 -> 5]
        # n = 6 
        #[0:[1, 2]], 1:[3, 5], 2:[], 3:[4], 4:[], 5:[4]]
        hashmap = {}
        visited = set()
        for i in range(numCourses):
            hashmap[i] = []

        for c, pre in prerequisites:
            hashmap[c].append(pre)
        
        def dfs(c):
            if c in visited:
                return False
            
            if hashmap[c] == []:
                return True

            visited.add(c)
            for course in hashmap[c]:
                if not dfs(course):
                    return False
                    
            visited.remove(c)
            hashmap[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False 
        return True
        

        