class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        current = 1
        longest  = 1
        if len(nums) == 1:
            return 1    
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                current += 1
                longest = max(longest,current)
            else:
                current = 1
        return longest            
