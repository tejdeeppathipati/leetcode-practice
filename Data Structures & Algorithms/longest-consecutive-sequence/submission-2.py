class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        unique = set(nums)

        for num in unique:
            if (num - 1) not in unique:
                count = 1
                while (num + count) in unique:
                    count = count + 1
                result = max(result, count)
        return result 