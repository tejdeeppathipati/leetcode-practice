class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1 
        highest = 0
        while left < right:
            low = min(heights[left], heights[right])
            highest = max(low * (right - left), highest)
            if heights[left] == low:
                left += 1
            if heights[right] == low:
                right -= 1
        return highest