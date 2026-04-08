class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        indarr = [0] * len(temperatures)
        for i,j in enumerate(temperatures):
            while stack and j > stack[-1][0]:
                stackT,stackme = stack.pop()
                indarr[stackme] = i - stackme
            stack.append((j,i))
        return indarr



        
        