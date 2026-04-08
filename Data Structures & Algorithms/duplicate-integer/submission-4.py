class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset1 = set()
        for i in range(len(nums)):
            if nums[i] in hashset1:
                return True
            else:
                hashset1.add(nums[i])
        return False