class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        val = 0
        for num in nums:
            longest = 1
            while (num+1) in nums:
                longest += 1
                num = num + 1

            val = max(longest, val)
        return val


        
        