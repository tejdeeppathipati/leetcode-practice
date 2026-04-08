class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mehash = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mehash:
                return [mehash[diff] ,  i]
            else:
                mehash[nums[i]] = i
                                     

        