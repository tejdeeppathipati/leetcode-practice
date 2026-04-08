class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        unique = set(nums)

        for num in unique:
            count = 1
            if (num - 1) not in unique:
                while (num + 1) in unique:
                    count +=1
                    num = num + 1
            result = max(result, count)
        return result
            
