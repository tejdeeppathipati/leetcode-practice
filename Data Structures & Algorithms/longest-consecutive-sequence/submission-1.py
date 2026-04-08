class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        unique = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in unique:
                streak += 1
                curr +=1 
            result = max(result,streak)
        return result