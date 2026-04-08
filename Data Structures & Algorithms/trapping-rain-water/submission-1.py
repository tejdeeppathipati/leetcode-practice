class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxL = height[left]
        maxR = height[right]

        total = 0

        while left < right:
            if maxL < maxR:
                left += 1
                maxL = max(maxL, height[left])
                cap = maxL - height[left]
                if cap > 0:
                    total += cap 
            else:
                right -= 1
                maxR = max(maxR, height[right])
                cap = maxR - height[right]
                if cap > 0:
                    total += cap 
        return total

            


            
