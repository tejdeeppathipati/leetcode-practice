class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) -1
        water = 0
        left_max = 0
        right_max = 0
        while L < R:
            if height[L] <= height[R]:
                if height[L] >= left_max:
                    left_max = height[L]
                else:
                    water += left_max - height[L]
                L+=1
            else:
                if height[R] >= right_max:
                        right_max = height[R]
                else:
                    water += right_max - height[R]
                R-=1
        return water               

        
                       


            

        