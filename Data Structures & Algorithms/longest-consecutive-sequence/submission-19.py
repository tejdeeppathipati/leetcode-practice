class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        val = 0
        for num in nums:
            if (num - 1) not in numSet:
                longest = 1
                while (num+1) in nums:
                    longest += 1
                    num = num + 1

                val = max(longest, val)
        return val


        
        