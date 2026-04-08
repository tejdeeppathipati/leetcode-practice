class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        final_list = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue 
                twoSum = nums[i] + nums[j]
                l, r = j + 1, n - 1
                while l < r:
                    total = twoSum + nums[l] + nums[r]
                    if total < target:
                        l += 1
                    elif total > target:
                        r -= 1
                    else:
                        final_list.append([nums[i], nums[j], 
                                            nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1
                        while nums[r] == nums[r - 1] and l < r:
                            r -= 1
        return final_list





            
        