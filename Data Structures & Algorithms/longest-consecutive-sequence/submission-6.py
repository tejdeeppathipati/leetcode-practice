class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq = set(nums)
        out = 0 
        for num in uniq:
            curr, count = num, 1
            if num - 1 not in uniq:
                while curr + 1 in uniq:
                    curr += 1
                    count += 1
                out = max(count, out)
        return out 
        