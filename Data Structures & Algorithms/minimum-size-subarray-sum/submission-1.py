class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSize = float("inf")
        l , r = 0, 0 
        currSum = 0
        while r < len(nums):
            if currSum < target:
                currSum += nums[r]
                r += 1
            while currSum >= target:
                minSize = min(minSize, (r - l))
                currSum -= nums[l]
                l += 1

        if minSize == float("inf"):
            return 0

        return minSize