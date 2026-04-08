class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = 0 
        n = len(nums) - 1
        i = 1
        while i <= n:
            while (i < n) and (nums[prev] == nums[i]):
                i += 1
            if i == n and (nums[prev] == nums[i]):
                return prev + 1
            prev += 1
            nums[prev] = nums[i]
            i += 1
        return prev + 1




            