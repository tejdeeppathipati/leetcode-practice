class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        final = [0] * len(nums)
        pre, post = 1, 1 
        for i in range(len(nums)):
            prefix[i] = nums[i] * pre
            pre = nums[i] * pre
        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = nums[i] * post
            post = nums[i] * post
        for i in range(len(nums)):
            if i == 0:
                final[i] = postfix[i + 1]
            elif i == (len(nums) - 1):
                final[i] = prefix[i - 1]
            else:
                final[i] = prefix[i - 1] * postfix[i + 1]
        return final 

