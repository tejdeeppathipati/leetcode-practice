class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 3, 4] --> product of all the numbers / number 
        # [1, 1, 2, 6]
        # [24, 12, 8, 6]
        n = len(nums)
        result = [1] * n
        postfix = nums[n - 1]

        for i in range(1, n):
            result[i] = nums[i - 1] * result[i - 1]
        
        for i in range(n-2, -1, -1):
            result[i] *= postfix
            postfix *= nums[i] 

        return result