class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        # n is current numner in numset
        for n in numset:
            if (n-1) not in numset:
                curr = 1
                while (n + curr) in numset:
                    curr += 1
                longest = max(longest, curr)
        return longest
                  
