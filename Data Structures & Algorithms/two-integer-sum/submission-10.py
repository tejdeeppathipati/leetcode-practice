class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = [4, 5, 6, 7, 8], target = 12
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]== target:
                    return [i,j]



            
    
        