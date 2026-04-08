class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        minSize = float("inf")
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                minSize = min(minSize, right - left + 1)
                total -= nums[left]
                left += 1
        if minSize == float("inf"):
            minSize = 0 
        return minSize
            


            

