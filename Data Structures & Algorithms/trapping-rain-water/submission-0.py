class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        if n == 0:
            return 0

        rightmax, leftmax, result = [0] * n,  [0] * n, 0

        leftmax[0], rightmax[n- 1] = height[0], height[n - 1]
        for i in range(1, n):
            leftmax[i] = max(leftmax[i-1], height[i])

        for i in range(n - 2, - 1, -1):
            rightmax[i] = max(rightmax[i + 1], height[i])  
    
        for i in range(n):
            val = (min(rightmax[i], leftmax[i])) - height[i]
            if val >= 0:
                result += val
        return result 
                

            
            
