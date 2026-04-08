class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        is_zero = False
        count = 0
        output = [0] * len(nums)
        for num in nums:
            if num != 0:
                product *= num
            else:
                is_zero = True
                count += 1
        if count > 1 or count == len(nums):
                return output

        for i in range(len(nums)):
            if (is_zero):
                if (nums[i] != 0):
                    output[i] = 0
                else:
                    output[i] = product
            else:
                output[i] = int(product/nums[i])
        return output
