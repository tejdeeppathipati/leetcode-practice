class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newarr = []
        mul  = 1
        count_x = nums.count(0)

        if count_x > 1:
            return [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                mul = mul * nums[i]

        for i in range(len(nums)):
            if nums[i] == 0:
                newarr.append(mul)
            else:
                newarr.append(mul // nums[i] if count_x == 0 else 0)
        return newarr        
        